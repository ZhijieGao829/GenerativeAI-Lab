# **OpenAI API Development Environment Setup**

This tutorial walks you through setting up a development environment to interact with the OpenAI API using Python. While we **recommend** using **Anaconda** to manage your environment, the core requirement is having **Python** installed. We'll guide you through installing the necessary libraries to make requests to OpenAI's API.

---

## **Prerequisites**

1. **OpenAI Account**:
   - Sign up for an OpenAI account [here](https://platform.openai.com/signup).
   - After signing up, navigate to the [API Keys page](https://platform.openai.com/account/api-keys) to create and retrieve your API key.

2. **Python**:
   - If you're **not using Anaconda**, you must install **Python 3.8+**. Download it from the [official Python website](https://www.python.org/downloads/).
   - If you're using **Anaconda**, Python comes included with the installation.

3. **Anaconda (Recommended)**:
   - Anaconda simplifies environment management by providing an all-in-one solution. If you'd like to use it, follow the [official Anaconda installation guide](https://docs.anaconda.com/anaconda/install/).

---

## **Steps to Set Up Your Environment**

### **Step 1: Install Python**

- If you're **not using Anaconda**, download and install Python 3.8+ from the [official Python website](https://www.python.org/downloads/).
- Verify your Python installation by running the following command:
    ```bash
    python --version
    ```

### **Step 2 (Recommended): Use Anaconda to Create and Activate a New Environment**

If you prefer using Anaconda for environment management:

1. **Create a new environment** with Python 3.8+:
    ```bash
    conda create --name openai-env python=3.11
    ```

2. **Activate the environment**:
    ```bash
    conda activate openai-env
    ```

<<<<<<< HEAD
If you're **not using Anaconda**, you can create a virtual environment with Python:

1. **Create a virtual environment**:
    ```bash
    python -m venv openai-env
    ```

2. **Activate the environment**:
    - On macOS/Linux:
      ```bash
      source openai-env/bin/activate
      ```
    - On Windows:
      ```bash
      openai-env\Scripts\activate
      ```

---

=======
>>>>>>> 9673e11889f3ced228d202b9abf794a0d206b03a
### **Step 3: Install the OpenAI Python Library**

Once your environment is activated (whether through Anaconda or `virtualenv`), install the OpenAI Python client library:

```bash
pip install --upgrade openai
```

### **Step 4: Set Your OpenAI API Key**

To make API requests, you need to set your OpenAI API key as an environment variable.

#### **Mac/Linux**:

1. Open your terminal and edit your profile file (`.bash_profile` or `.zshrc` for zsh users):
    ```bash
    nano ~/.bash_profile
    ```
   Or for Zsh:
    ```bash
    nano ~/.zshrc
    ```

2. Add the following line to the file, replacing `your-api-key-here` with your actual OpenAI API key:
    ```bash
    export OPENAI_API_KEY="your-api-key-here"
    ```

3. Save the file (`Ctrl+O` to save, `Ctrl+X` to exit).
4. Load the changes:
    ```bash
    source ~/.bash_profile  # Or: source ~/.zshrc
    ```

5. Verify that your API key is set by running:
    ```bash
    echo $OPENAI_API_KEY
    ```

#### **Windows**:

1. Open the **Start Menu**, search for "Environment Variables", and select **Edit the system environment variables**.
2. In the **System Properties** window, click on **Environment Variables**.
3. Under **System Variables**, click **New** and add:
    - **Variable Name**: `OPENAI_API_KEY`
    - **Variable Value**: Your OpenAI API key
4. Press **OK** to save.
5. To verify, open the Command Prompt and run:
    ```bash
    echo %OPENAI_API_KEY%
    ```

---

### **Step 5: Make Your First API Request**

Now that your environment is set up, you can test your OpenAI API connection by creating a simple Python script.

1. Create a file named `openai_test.py` in your preferred editor or terminal/command prompt.
2. Add the following code:

    ```python
    import openai
    import os

    # Retrieve the API key from the environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Create a chat completion request
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is OpenAI?"}
        ]
    )

    # Print the response
    print(completion.choices[0].message['content'])
    ```

3. Run the script in the terminal:
    ```bash
    python openai_test.py
    ```

4. You should see a response from OpenAI GPT-3.5 Turbo in your terminal.


---

## **Additional Resources**

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Documentation](https://docs.python.org/3/)
- [Anaconda Documentation](https://docs.anaconda.com/)
