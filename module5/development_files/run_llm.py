"""Practice 5.2 - run one Hugging Face causal language model on a GPU.

Usage (inside the Kubernetes Job):
    python3 /data/hf_practice/run_llm.py --model phi3
"""
import argparse
import os
import time
from datetime import datetime

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Models that do NOT need gated access. Key -> Hugging Face model ID.
MODELS = {
    "phi3": "microsoft/Phi-3-mini-4k-instruct",          # 3.8B, instruct (default)
    "tinyllama": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",   # 1.1B, chat
    "qwen25": "Qwen/Qwen2.5-7B-Instruct",                # 7B, instruct
    "stablelm2": "stabilityai/stablelm-2-1_6b",          # 1.6B, base (no chat template)
}

PROMPTS = [
    "Write down a paragraph about University of Missouri.",
    "Tell me something interesting about Columbia in Missouri",
    "Are you familiar with the Institute for Data Science and Informatics at the University of Missouri",
    "What programs are available at the Institute for Data Science and Informatics at the University of Missouri",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="phi3", choices=sorted(MODELS))
    parser.add_argument("--max-new-tokens", type=int, default=300)
    parser.add_argument("--out-dir", default="/data/hf_practice/outputs")
    args = parser.parse_args()
    model_id = MODELS[args.model]

    print(f"PyTorch {torch.__version__} | CUDA available: {torch.cuda.is_available()}", flush=True)
    if not torch.cuda.is_available():
        raise SystemExit("No GPU visible. Check the nvidia.com/gpu lines in the Job YAML.")
    props = torch.cuda.get_device_properties(0)
    print(f"GPU: {props.name} | {props.total_memory / 1e9:.1f} GB", flush=True)
    print(f"HF cache: {os.environ.get('HF_HOME', '(default)')}", flush=True)

    t0 = time.time()
    print(f"Loading {model_id} ...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    try:
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", dtype="auto")
    except TypeError:  # older transformers versions use torch_dtype
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", torch_dtype="auto")
    print(f"Loaded in {time.time() - t0:.0f} s | GPU memory used: "
          f"{torch.cuda.memory_allocated() / 1e9:.1f} GB", flush=True)

    os.makedirs(args.out_dir, exist_ok=True)
    out_path = os.path.join(
        args.out_dir, f"{args.model}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

    with open(out_path, "w") as f:
        for i, prompt in enumerate(PROMPTS, start=1):
            if tokenizer.chat_template:  # instruct/chat models
                text = tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    tokenize=False, add_generation_prompt=True)
            else:                        # base models: plain text continuation
                text = prompt
            inputs = tokenizer(text, return_tensors="pt", add_special_tokens=False).to("cuda")
            t1 = time.time()
            with torch.no_grad():
                output = model.generate(**inputs, max_new_tokens=args.max_new_tokens,
                                        do_sample=False, pad_token_id=tokenizer.eos_token_id)
            answer = tokenizer.decode(output[0][inputs["input_ids"].shape[1]:],
                                      skip_special_tokens=True).strip()
            block = (f"\n=== Prompt {i} ({time.time() - t1:.1f} s) ===\n"
                     f"Q: {prompt}\nA: {answer}\n")
            print(block, flush=True)
            f.write(block)

    print(f"Saved results to {out_path}", flush=True)


if __name__ == "__main__":
    main()
