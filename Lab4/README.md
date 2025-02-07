# Text-to-Image Generation with Hugging Face and OpenAI

This repository provides guidance for using text-to-image generation models, specifically Stable Diffusion from Hugging Face and DALL·E from OpenAI. We will cover setup and steps to generate images using both platforms.

---

## Table of Contents
1. [Setup](#setup)
2. [Using Hugging Face for Stable Diffusion](#using-hugging-face-for-stable-diffusion)
3. [Using OpenAI for DALL·E](#using-openai-for-dalle)
4. [Additional Resources](#additional-resources)

---

## Setup
### Prerequisites
- Python 3.8 or higher
- A Google Colab account (recommended for GPU access)
- Hugging Face and OpenAI API keys

### Installation
Before proceeding, ensure you have the necessary packages installed. Use the following commands:
```bash
pip install diffusers transformers accelerate huggingface_hub
```

---

## Using Hugging Face for Stable Diffusion

### 1. Access the Model on Hugging Face
- Navigate to the [Stable Diffusion 3.5 Large Model page](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) on Hugging Face. If access is restricted, you may need to agree to the model’s terms of service to proceed.
- While I'm using the "Stable Diffusion 3.5 Large Model" for demonstration purposes in this lab, you are encouraged to explore and utilize other available models. For a broader selection of models, check out the [Hugging Face model directory](https://huggingface.co/models?pipeline_tag=text-to-image), which offers various options tailored to different text-to-image generation tasks.

### 2. Create a Hugging Face API Token
1. Go to your [Hugging Face account settings](https://huggingface.co/settings/tokens).
2. Create a new access token with the following permissions:
   - **Inference**: Make calls to the serverless Inference API.
   - **Repositories**: Read access to public gated repos.
3. Save this token securely.

### 3. Set Up Your Environment
Open Google Colab and select a GPU:
1. Navigate to **Runtime > Change runtime type**.
2. Select **T4 GPU** under *Hardware accelerator*.
3. Click **Save**.

### 4. Authenticate with Hugging Face
In your Colab notebook, authenticate with your API token:
```python
from huggingface_hub import login
login("YOUR_HUGGINGFACE_API_TOKEN")
```

### 5. Load and Run Stable Diffusion
Here’s a sample code snippet to generate an image:
```python
import torch
from diffusers import StableDiffusion3Pipeline

# Load the model and set precision for efficiency
pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3.5-large",
    torch_dtype=torch.bfloat16  # Use torch.float16 if needed
)
pipe = pipe.to("cuda")  # Move the model to GPU

# Generate the image
image = pipe(
    "Andrew Carnegie holding an apple in his left hand, while driving a Mercedes-Benz G-Wagon G63",
    num_inference_steps=6,
    guidance_scale=3.5
).images[0]

# Save the generated image
image.save("Carnegie.png")
```

### 5. Image Generation Result
<img src="https://github.com/mtbogush/GenerativeAI-Lab/blob/f153086f469c13314e5340fe3b82b0da04e88b5a/Lab3/Images/Carnegie_HF.png?raw=true" width="600" height="600" alt="Carnegie Dall-E">



---

## Using OpenAI for DALL·E

### 1. Set Up Your OpenAI API Key
Before you start, you'll need an API key from OpenAI:
- Visit the [OpenAI API platform](https://platform.openai.com/signup) and sign up if you haven't already.
- Once registered and logged in, navigate to the API keys section and generate a new API key.
- Store this API key securely, typically in an environment variable:
  ```bash
  export OPENAI_API_KEY='your-api-key-here'
  ```

### 2. Install the OpenAI Python Package
Use pip to install the OpenAI Python client library:
```bash
pip install openai
```

### 3. Initialize the OpenAI Client
Set up the OpenAI client in your Python script using the stored API key:
```python
import openai

# Initialize the OpenAI client with your API key
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### 4. Using the DALL-E Model to Generate Images
Here’s how to generate an image from a text prompt using DALL-E:
```python
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Andrew Carnegie holding an apple in his left hand, while driving a Mercedes-Benz G-Wagon G63",
  size='1024x1024',
  quality="hd",
  n=1
)

image_url = response.data[0].url
print(image_url)
```
- The image URL will be printed to the console. You can use this URL to view or download the image as needed. URL will expire after a certain period of time, so make sure you download the photo if you need it saved.
### 5. Image Generation Result
<img src="https://github.com/mtbogush/GenerativeAI-Lab/blob/f153086f469c13314e5340fe3b82b0da04e88b5a/Lab3/Images/Carnegie_Dall-E.png?raw=true" width="600" height="600" alt="Carnegie Dall-E">

### Additional Notes:
- For comprehensive documentation and more examples, visit the [OpenAI API documentation](https://beta.openai.com/docs/).

---


## Additional Resources
- [Hugging Face Documentation](https://huggingface.co/docs)
- [OpenAI Documentation](https://platform.openai.com/docs)
