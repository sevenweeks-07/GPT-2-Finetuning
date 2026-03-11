# GPT-2 Fine-Tuning 🤖

A personal project focused on learning the fundamentals of fine-tuning Large Language Models (LLMs). In this repository, I successfully fine-tuned a lightweight GPT-2 model to understand and generate text based on a conversational dataset.

## 📌 Project Overview
The entire training pipeline was built and executed in a Google Colab notebook using a T4 GPU. 

* **Base Model:** `distilgpt2` (a smaller, faster version of GPT-2).
* **Dataset:** `mlabonne/guanaco-llama2-1k`.
* **Training Method:** Supervised Fine-Tuning (SFT) using the `trl` library.

## 🛠️ Tech Stack & Libraries
* **PyTorch:** Backend deep learning framework.
* **Hugging Face `transformers`:** For loading the pre-trained model and tokenizer.
* **Hugging Face `datasets`:** For downloading and formatting the training data.
* **Hugging Face `trl` (Transformer Reinforcement Learning):** Used the `SFTTrainer` and `SFTConfig` classes to streamline the training loop.

## 🚀 Key Features & Optimizations
To successfully train the model on consumer-grade hardware (Google Colab free tier) without running out of memory, I implemented a few crucial optimizations:
* **Gradient Accumulation:** Kept the `per_device_train_batch_size` at `2` to save VRAM, but accumulated gradients over `8` steps to simulate a larger, more stable batch size of 16.
* **FP16 Mixed Precision:** Enabled 16-bit floating point precision (`fp16=True`) to cut memory usage in half and speed up training.
* **Cosine Learning Rate Scheduler:** Used to smoothly decrease the learning rate over time, allowing the model to gently settle on the optimal weights.

## 💻 How to Run
1. Open the `gpt2_finetuning.ipynb` notebook in Google Colab.
2. Ensure your Colab runtime is set to **GPU (T4)**.
3. Run the cells sequentially to install dependencies, load the dataset, configure the memory hacks, and start the training loop.