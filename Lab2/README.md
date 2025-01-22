# Lab 2: Introduction to Prompt Engineering

Welcome to Lab 2! In this lab, you'll explore prompt engineering, a powerful technique for effectively interacting with large language models (LLMs) like OpenAI's GPT series. By mastering the art of crafting prompts, you can guide these models to produce more relevant, accurate, and creative outputs across a wide range of tasks.

## What is Prompt Engineering?

Prompt engineering is the process of designing and refining prompts to elicit desired responses from language models. By carefully structuring your prompts with specific instructions, context, and examples, you can influence the model's output to better suit your needs in tasks such as text generation, translation, summarization, and question answering.

## OpenAI Model Parameter Explanation
In the provided code snippet, you are configuring the AI model's behavior for generating text responses. These settings, known as **hyperparameters**, are crucial for steering the model's response generation process. Hyperparameters play a pivotal role in adjusting how the model interprets and processes the input it receives. While there are many hyperparameters available, the ones mentioned here are particularly important to understand for effective use:


- **model**: Specifies which model to use. Different models have different capabilities, sizes, and cost implications.
- **messages**: The input prompt or conversation history sent to the model for generating a response.
- **temperature**: Controls randomness in the response generation. A lower temperature (e.g., 0.1) makes the model's responses more deterministic and conservative.
- **max_tokens**: The maximum length of the response the model can generate, measured in tokens (words or pieces of words).
- **top_p**: Controls the diversity of the responses through nucleus sampling, where `top_p` is the probability mass considered for sampling tokens. A value of 1 means considering all tokens, thus reducing constraints on generation diversity.


### Quick Example

Consider the sentence "I am heading towards" as input, and our model aims to predict the next word given these previous words.
With all those fancy transformers stuff, we end up having a few options with the following probs:

1. home: 0.4
2. school: 0.3
3. the park: 0.2
4. Mars: 0.1


## Temperature:

Low temperature (0.1): The model skews strongly toward the most probable option. In this case, "home" (0.4) would almost always be chosen.

High temperature (1.0): The model’s selection becomes more random, with less emphasis on probabilities. It might select any of the options (“home”, “school,” “the park,” or “Mars”), giving each word a chance proportional to its probability.

## Top-p:

Top-p = 1.0 (Full Nucleus): All options are considered. The model might choose any of the four words, weighted by their respective probabilities. So you might be head towards Mars 1/10.

Top-p = 0.7: Only the top cumulative 70% probability is considered. In this case, "home" and "school" would be included, but "the park" and "Mars" would be excluded because their combined probability (0.3) falls outside the 60% threshold. So you will never head towards Mars under this hyperparam!

## max_tokens:

If max_tokens is set to 1, the model stops after generating a single word. For the prompt "I am heading towards," the output might be "home."

With max_tokens = 5, the model can produce a longer response, such as:
"home to finish my homework before dinner."


### Example Python Script

```python
# Make the API request using the defined prompt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Model identifier
    messages=prompt,        # Input prompt or messages
    temperature=0.1,        # Lower temperature for less randomness
    max_tokens=250,         # Maximum length of the generated response
    top_p=1                 # Use all tokens in the response generation
)
```


## Key Prompting Techniques

In this lab, you'll learn about three essential prompting techniques:

1. **Zero-Shot Prompting**
2. **Few-Shot Prompting**
3. **Chain-of-Thought Prompting**

These techniques offer different ways to interact with an LLM, each with its unique advantages depending on the task.

### 1. Zero-Shot Prompting

Zero-shot prompting involves asking the model to perform a task without providing any examples. You give a clear and direct instruction, and the model generates a response based on its understanding and knowledge.

**Example:**

**Prompt:**

**System Message:** "You will be provided with sentences in English, and your task is to translate them into French."
- *This serves as the instruction, telling the model what the task is. It sets the context for what the model needs to do.*

**User Message:** "My name is Michael. What is yours?"
- *This is the input that needs to be processed according to the task defined in the system message. In this case, translating the sentence from English into French.*

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with sentences in English, and your task is to translate them into French."
    },
    {
      "role": "user",
      "content": "My name is Michael. What is yours?"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

# Print the response
print(response.choices[0].message.content)
```

**Model Output:**

"Je m'appelle Michael. Et toi, comment t'appelles-tu?"

**Use Case:**

Ideal for straightforward tasks that the model is likely familiar with and doesn't require additional context or examples.

### 2. Few-Shot Prompting

Few-shot prompting provides the model with a few examples within the prompt to guide its response. This helps the model understand the pattern or format you expect.

**Example:**

**Prompt:**

**System Message:** "Correct the following sentences for grammatical errors."
- *This instruction sets the task for the model, clearly specifying that its job is to correct grammatical mistakes in the provided sentences.*

**User Message:** "She don't like apples."
- *This is an example input sentence given to the model, which contains a grammatical error for the model to correct.*

**Assistant Message:** "She doesn't like apples."
- *This is the model's corrected response, demonstrating the appropriate grammatical structure.*

**User Message:** "We was going to the park."
- *Another example requiring grammatical correction, further guiding the model on the task expectations.*

**Assistant Message:** "We were going to the park."
- *The model provides the corrected form, showing how to correct the verb tense.*

**User Message:** "He have two cats."
- *This sentence introduces a different type of grammatical error for the model to address.*

**Assistant Message:** "He has two cats."
- *Corrects the verb agreement error, further training the model.*

**User Message:** "They is coming over later."
- *Presents a final grammatical challenge in the few-shot sequence.*

```python
from openai import OpenAI
client = OpenAI()

# Define the prompt with several examples and a new sentence for correction
prompt = [
    {
        "role": "system",
        "content": "Correct the following sentences for grammatical errors:"
    },
    {
        "role": "user",
        "content": "She don't like apples."
    },
    {
        "role": "assistant",
        "content": "She doesn't like apples."
    },
    {
        "role": "user",
        "content": "We was going to the park."
    },
    {
        "role": "assistant",
        "content": "We were going to the park."
    },
    {
        "role": "user",
        "content": "He have two cats."
    },
    {
        "role": "assistant",
        "content": "He has two cats."
    },
    {
        "role": "user",
        "content": "They is coming over later."
    }
]

# Make the API request using the defined prompt
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=64,
    top_p=1
)

# Print the corrected sentence
print(response.choices[0].message.content)
```

**Model Output:**

"They are coming over later."

**Explanation:**

By including several examples, you help the model infer the task and produce a response that matches the provided pattern.

**Use Case:**

Useful for tasks that require specific formatting, style, or when the model needs to follow a particular pattern or logic.

### 3. Chain-of-Thought Prompting

Chain-of-thought prompting encourages the model to think through the problem by generating intermediate reasoning steps before arriving at a final answer. This is especially helpful for complex tasks that require reasoning or multi-step calculations.

**Example:**

**Prompt:**

**System Message:** "Determine if the sum of odd numbers in each group is even or odd, and explain your reasoning step by step."
- *This sets the task for the model, specifying not only what to determine (whether the sum of odd numbers is even or odd) but also to provide a detailed explanation of the reasoning behind the answer.*

**User Message:**
- *Includes multiple examples where the model is given a set of numbers and asked to identify odd numbers, calculate their sum, and determine if the sum is even or odd. Each example is followed by an explanation of how the conclusion was reached.*

**Example Detail:**

- **Question:** "The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1."
- **Explanation:** "First, identify the odd numbers in the list, which are 9, 15, and 1. Then, add these numbers together: 9 + 15 + 1 = 25. Check if 25 is even or odd. Since 25 is odd, the statement is false."
- **Answer:** "False."

- **Further Questions:** Continue with additional questions, each followed by a detailed reasoning process and conclusion, teaching the model the expected pattern of reasoning and output.

```python
from openai import OpenAI
client = OpenAI()

# Define the prompt with several examples and a new sentence for correction
prompt = [
    {
        "role": "system",
        "content": "Determine if the sum of odd numbers in each group is even or odd, and explain your reasoning step by step."
    },
    {
        "role": "user",
        "content": """
        Question: The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
        Explanation: First, identify the odd numbers in the list, which are 9, 15, and 1. Then, add these numbers together: 9 + 15 + 1 = 25. Check if 25 is even or odd. Since 25 is odd, the statement is false.
        Answer: False.
        
        Question: The odd numbers in this group add up to an even number: 17, 10, 19, 4, 8, 12, 24.
        Explanation: Identify the odd numbers, which are 17 and 19. Add these numbers: 17 + 19 = 36. Check if 36 is even or odd. Since 36 is even, the statement is true.
        Answer: True.
        
        Question: The odd numbers in this group add up to an even number: 16, 11, 14, 4, 8, 13, 24.
        Explanation: The odd numbers are 11 and 13. Adding them gives 11 + 13 = 24. Check if 24 is even or odd. Since 24 is even, the statement is true.
        Answer: True.
        
        Question: The odd numbers in this group add up to an even number: 17, 9, 10, 12, 13, 4, 2.
        Explanation: The odd numbers here are 17, 9, and 13. Adding these gives 17 + 9 + 13 = 39. Check if 39 is even or odd. Since 39 is odd, the statement is false.
        Answer: False.
        
        Question: The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
        Explanation:
        Answer:
        """
    }
]


# Make the API request using the defined prompt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=prompt,
    temperature=.1,
    max_tokens=500,
    top_p=1
)

# Print the model's reasoning and answer for the last question
print(response.choices[0].message.content)
```

**Model Output:**

Question: The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.

Explanation: Identify the odd numbers in the list, which are 15, 5, 13, 7, and 1. Add these numbers together: 15 + 5 + 13 + 7 + 1 = 41. Check if 41 is even or odd. Since 41 is odd, the statement is false.

Answer: False.

**Explanation:**

By instructing the model to "think step by step," you encourage it to break down the problem and show the reasoning process, leading to more accurate and explainable answers.

**Use Case:**

Ideal for mathematical problems, logical reasoning, or any task that benefits from a step-by-step approach.

## Experimentation

Feel free to experiment with these prompting techniques:

- **Zero-Shot Prompting:** Try asking the model to perform a task without any examples and observe how it responds.
- **Few-Shot Prompting:** Modify the examples or add new ones to see how they influence the model's output.
- **Chain-of-Thought Prompting:** Encourage the model to explain its reasoning process for complex questions.

## Additional Prompt Engineering Strategies

To further enhance your interactions with LLMs, consider the following strategies:

- **Provide Clear Instructions:** Be specific about what you want the model to do. Ambiguous prompts can lead to less accurate responses.
- **Use Delimiters:** Clearly separate different parts of your prompt using symbols or formatting (e.g., quotation marks, brackets, or triple backticks).
- **Specify the Desired Output Format:** If you need the response in a particular format (e.g., a list, JSON, or a specific style), mention it explicitly in your prompt.
- **Set the Role or Persona:** Instruct the model to adopt a specific role to guide the tone and style of the response (e.g., "You are a helpful assistant," or "Act as a professional translator").
- **Ask for Step-by-Step Solutions:** For complex tasks, request that the model provides a detailed explanation or reasoning process.

## Additional Resources

- **[OpenAI API Prompt Engineering Documentation](https://platform.openai.com/docs/guides/prompt-engineering):** Learn more about OpenAI API best prompting strategies.
- **[OpenAI API Prompt Engineering Examples](https://platform.openai.com/docs/examples):** OpenAI Prompt engineering examples.
- **[OpenAI API Models](https://platform.openai.com/docs/models):** OpenAI available models to use.
- **[OpenAI API Model Pricing](https://openai.com/api/pricing/):** OpenAI model pricing.
- **[OpenAI API Model Rate Limits](https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free):** OpenAI model Rate Limits.
- **[Prompt Engineering Guide](https://www.promptingguide.ai/):** Explore comprehensive strategies and examples for effective prompt engineering.

