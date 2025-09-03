from modu_muse import Pipeline

pipe = Pipeline(
    llm_name="mistralai/Mistral-7B-Instruct-v0.2",
    vision_name="openai/clip-vit-base-patch16"
)

result = pipe.infer("path/to/image.jpg", "Describe the scene.")
print(result)
