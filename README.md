
# 🧠 ModuMuse

**Modular Multimodal Intelligence**  
Plug any Hugging Face LLM and vision encoder together via a learnable projector.  
Supports zero-shot inference today, and adapter-based fine-tuning tomorrow.

<p align="center">
  <a href="https://github.com/ELkarousWissem/ModuMuse">
    <img src="https://img.shields.io/github/stars/ELkarousWissem/ModuMuse?style=social" alt="GitHub stars">
  </a>
  <a href="https://pypi.org/project/modu-muse/">
    <img src="https://img.shields.io/pypi/v/modu-muse?color=blue" alt="PyPI version">
  </a>
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python version">
</p>

---

## 🚀 Features

- 🔌 Plug-and-play architecture for combining LLMs and vision encoders
- 🧠 Supports popular models like Qwen, Mistral, LLaMA, CLIP, XCLIP, SAM
- 🧪 Zero-shot inference with learnable projector modules
- 🛠️ Adapter-based fine-tuning (coming soon)
- 📊 Easy benchmarking and visualization tools

---

## 📦 Installation

```bash
pip install modu-muse
```

---

## 🧬 Quick Start

```python
from modu_muse import Pipeline

pipe = Pipeline(
    llm_name="mistralai/Mistral-7B-Instruct-v0.2",
    vision_name="openai/clip-vit-base-patch16"
)

result = pipe.infer("path/to/image.jpg", "Describe the scene.")
print(result)
```

---

## 🧠 Architecture

```text
[Image/Video] → [Vision Encoder] → [Projector] → [LLM]
```

- Vision encoder extracts features
- Projector maps visual features to LLM-compatible embeddings
- LLM generates text conditioned on visual context

---

## 🛠️ Fine-Tuning (Coming Soon)

Train your own projector using paired image-text datasets:

```bash
python train_adapter.py \
  --model llm=Qwen1.5 vision=xclip \
  --dataset_path ./data/relevance_dataset \
  --output_dir ./checkpoints
```

---

## 📁 Project Structure

```
modu_muse/
├── pipeline.py          # Main multimodal pipeline
├── projector.py         # Vision-to-LLM projector
├── models/
│   ├── llm.py           # LLM loader
│   ├── vision.py        # Vision encoder loader
├── examples/
│   └── quick_start.py   # Demo script
```

---

## 🤝 Contributing

We welcome contributions! Whether it's new model support, training scripts, or documentation improvements—open a PR or start a discussion.

---

## 📜 License

This project is licensed under the **MIT License**.  
© 2025 [Wissem Elkarous](https://github.com/ELkarousWissem)

---

## 🌐 Resources

- 🔗 [Hugging Face Transformers](https://huggingface.co/transformers/)
- 🔗 [CLIP & XCLIP Models](https://huggingface.co/models?search=clip)
- 🔗 [Qwen LLMs](https://huggingface.co/Qwen)

---

<p align="center">
  <em>ModuMuse: Where vision meets language.</em>
</p>
