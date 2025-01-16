# **OpenAI API Development Environment Setup**

This tutorial walks you through setting up a development environment to interact with the OpenAI API using Python. While we **recommend** using **Anaconda** to manage your environment, the core requirement is having **Python** installed. We'll guide you through installing the necessary libraries to make requests to OpenAI's API.

---

## **Prerequisites**

1. **OpenAI Account**:
   - Sign up for an OpenAI account [here](https://platform.openai.com/signup).
   - After signing up, navigate to the [API Keys page](https://platform.openai.com/account/api-keys) to create and retrieve your API key.

---

## **Our Goal**

To Have a working python based environment so that you can make you first API call to OpenAi.

---

## **Our Options**

This is not a coding class, so we provide multiple options for you to get things started. Just like in real world, there are many options out there, and you should pick the option that makes most sense for you.

![5ecc3ce80a2d5a3d80bc2841d4a488a](https://github.com/user-attachments/assets/544b1cdb-6f5e-4430-8767-4219295ef620)

---


## **Steps to Set Up Your Environment**

### **Option 1: Just Python**

- If you're **not using Anaconda**, download and install Python 3.8+ from the [official Python website](https://www.python.org/downloads/).
- Verify your Python installation by running the following command (in command line/powershell):
    ```bash
    python --version
    ```
- You are free to choose your code editor. We recommend VSCode or PyCharm.

#### If you are going with option 1, the raw python way, this is the end for your tech setup 

### **Option 2: Lets Have Jupyter**

- Jupyter notebook has a number of advantages like easier workflow, better visualizations, the ability to run codes easily in blocks etc...
- Anaconda is by far the most standard way to get Jupyter installed and working, so we recommend this approach to setup Jupyter Notebook.
- [official Anaconda installation guide](https://docs.anaconda.com/anaconda/install/).
- Once you have Anaconda installed, it creates a SEPARATE python interpreter that is irrlevant to the python on your machine, and Jupyter comes with the default install options.
- Pull up Anaconda Prompt, and type Jupyter Notebook. It should show up in your default browser.


### **Option 3: Well I Prefer The Easier Way With Colab**

- Colab is a google based service that integrates Jupyter Notebook with the google ecosystem.
- Download Lab1_StarterNotebook.ipynb, and upload it to your personal google drive under a folder of your choice


### **Option 4: Huggingface Space**

- Functions similarly to google colab, though it is provided by Huggingface and we have an advanced version of it purchased.
- Create a Huggingface account, and Create New Space under the Spaces Tab.
- In the setup options, make sure you select ![ab1ba9fb36d45839e847c2fb1786287](https://github.com/user-attachments/assets/bb481de4-b5ad-4c57-a4ca-0d3183caede0)
- Download Lab1_StarterNotebook.ipynb, and upload it to your personal Huggingface Space.

- Later in the course, you would join our course huggingface spaces for some homeworks. Make sure that you CREATE COPIES of the starter code and work on the copied version in those spaces. Hugging Face lacks a well-structured permission management system, so if you mess up the starter code file, the entire class loses the starter code (and we have to upload one again, lots of confusion...)



### **Bonus: Use Anaconda to Create and Activate a New Environment**

If you prefer using Anaconda for environment management, follow these steps in the **Anaconda Prompt** or any terminal where `conda` is configured:

1. **Create a new environment** with Python 3.8+:
    ```bash
    conda create --name openai-env python=3.11
    ```

2. **Activate the environment**:
    ```bash
    conda activate openai-env
    ```

> **Note**: If you're using Anaconda, we recommend running these commands in the **Anaconda Prompt** or any terminal where `conda` commands are configured.
> **Note**: If you're using Windows with Anaconda and trying to setup virtual environments, you need a Linux subsystem for it. We recommend WSL, and are happy to provide support if you need.

A well known problem from previous semesters is that if you are going wiht virtual envirionments, you should restart the venv whenever you make changes to dependencies or your API key.

---
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

#### **Method 2: Using Jupyter Notebook or VS Code** (Suggested)

1. **Open the provided Jupyter notebook** in either Jupyter Notebook, VS Code, or any notebook-supported environment.

2. **Run the cells** to interact with the OpenAI API directly from the notebook environment.

3. You should receive similar output, with the model generating a response based on your request.

This allows you to test the API integration using both command-line and notebook-based workflows.

---

## **Additional Resources**

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI API Environment Documentation](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
- [Python Documentation](https://docs.python.org/3/)
- [Anaconda Documentation](https://docs.anaconda.com/)
