# Ssebowa
Ssebowa is free and open source library in Python that provides generative-ai models.

## Installation

Before running the script, ensure that the required libraries are installed. You can do this by executing the following commands:

```bash
git clone https://github.com/huggingface/diffusers
cd diffusers
pip install .

pip install ssebowa
````
 ## 🚀 Quick Start
- - -
# Ssebowa Image generation
### Finetuning on your own data

* Prepare about 10-20 high-quality photos (jpg or png) and put them in a specific directory.
* Please run on a machine with a GPU of 16GB or more. (If you're fine-tuning *SDXL*, you'll need 24GB of VRAM.)
```python
from ssebowa.dataset import LocalDataset
from ssebowa.model import SdSsebowaModel
from ssebowa.trainer import LocalTrainer
from ssebowa.utils.image_helpers import display_images
from ssebowa.utils.prompt_helpers import make_prompt

DATA_DIR = "data"  # The directory where you put your prepared photos
OUTPUT_DIR = "models"  

dataset = LocalDataset(DATA_DIR)
dataset = dataset.preprocess_images(detect_face=True)

SUBJECT_NAME = "<YOUR-NAME>"  
CLASS_NAME = "person"

model = SdSsebowaModel(subject_name=SUBJECT_NAME, class_name=CLASS_NAME)
trainer = LocalTrainer(output_dir=OUTPUT_DIR)
predictor = trainer.fit(model, dataset)
# Use the prompt helper to create an awesome AI avatar!
prompt = next(make_prompt(SUBJECT_NAME, CLASS_NAME))
images = predictor.predict(
    prompt, height=768, width=512, num_images_per_prompt=2,
)

display_images(images, fig_size=10)

```
### Image Generation
Ssebowa-Imagen is a python packaage that utilizes a combination of diffusion modeling and generative adversarial networks (GANs) to generate high-quality images from text descriptions. It leverages a 100 billion dataset of images and text descriptions, enabling it to accurately capture the nuances of real-world imagery and effectively translate text descriptions into compelling visual representations.
```python
from ssebowa import ssebowa_imgen
model = ssebowa_imgen.ssebowa_imgen()
# Generate an image with the text description "A cat sitting on a
bookshelf"
image = model.generate_image(text="A cat sitting on a bookshelf")
# Save the image to a file
image.save("cat_on_bookshelf.jpg")
```

# Ssebowa Vision Language Model

Ssebowa-vllm is an open-source visual large language model (VLLM) developed by
Ssebowa AI. It is a powerful tool that can be used to understand images.

```python
from ssebowa import ssebowa_vllm
model = ssebowa_vllm.ssebowa_vllm()

response =  model.understand(image_path, prompt)
print(response)
```
