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

If you prefer using Anaconda for environment management, follow these steps in the **Anaconda Prompt** or any terminal where `conda` is configured:

1. **Create a new environment** with Python 3.8+:
    ```bash
    conda create --name openai-env python=3.11
    ```

2. **Activate the environment**:
    ```bash
    conda activate openai-env
    ```

<<<<<<< HEAD
=======
> **Note**: You must use the **Anaconda Prompt**, **PowerShell (if conda is set up)**, or a terminal configured to use `conda` for these commands to work. If you try this in a standard command prompt without `conda` support, it may not recognize the commands.

---

>>>>>>> 0fca1143d29fe13f64c931ac6759027800396845
### **Step 3: Install the OpenAI Python Library**

Once your environment is activated (whether using Anaconda or installed Python), install the OpenAI Python client library:

```bash
pip install --upgrade openai
```

---

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

1. Open the **Start Menu** and search for "View advanced system settings". Select the result.
2. In the **System Properties** window, go to the **Advanced** tab.
3. Click the **Environment Variables** button at the bottom.
4. In the **Environment Variables** window, under **System Variables**, click **New** to create a new environment variable.
5. In the **New System Variable** window, enter:
   - **Variable Name**: `OPENAI_API_KEY`
   - **Variable Value**: Your OpenAI API key (replace with your actual key).
6. Click **OK** to save the new variable, and then press **OK** to close the **Environment Variables** window.
7. To verify the environment variable is set correctly, open **ADMINISTRATOR Command Prompt** and run:
   ```bash
   echo %OPENAI_API_KEY%
   ```
---

### **Step 5: Test Your First API Request Using Python Scripts and Notebooks**

Now that your environment is set up, you can test your OpenAI API connection using a Python script or Jupyter notebook.

#### **Method 1: Using a Python Script**

1. **Run the `Lab1_StarterPython.py` file** that has already been created for you in your project folder.

2. Open a terminal, navigate to your project directory, and execute the script by running:
    ```bash
    python Lab1_StarterPython.py
    ```

3. You should see a response from OpenAI GPT-3.5 Turbo in your terminal.

#### **Method 2: Using Jupyter Notebook or VS Code**

1. **Open the provided Jupyter notebook** in either Jupyter Notebook, VS Code, or any notebook-supported environment.

2. **Run the cells** to interact with the OpenAI API directly from the notebook environment.

3. You should receive similar output, with the model generating a response based on your request.

This allows you to test the API integration using both command-line and notebook-based workflows.

---

---

## **Additional Resources**

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Documentation](https://docs.python.org/3/)
- [Anaconda Documentation](https://docs.anaconda.com/)
