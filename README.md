Here is the complete `README.md` in markdown:

---

```markdown
# 🚀 AI Scenario Generator

An AI-powered scenario generator for creating visually rich, prompt-based scenarios for image and video generation. Built with a Python backend for AI logic and an Astro frontend for a clean, responsive user experience.

---

## 📁 Project Structure
```

project-root/
├── src/
│ ├── app.py # Python backend (FastAPI server)
│ ├── requirements.txt # Python dependencies
│ └── pages/
│ ├── index.astro # Main frontend page
│ └── api/
│ └── generate.js # API handler for frontend-backend communication
├── public/
│ └── favicon.ico
├── astro.config.mjs # Astro configuration
├── package.json # Frontend dependencies
└── README.md # Project documentation (this file)

````

---

## 🛠️ Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **Virtual Environment (Recommended)**

---

## 📦 Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/ai-scenario-generator.git
cd ai-scenario-generator
````

### **2. Backend Setup (Python)**

Navigate to the `src/` directory:

```bash
cd src
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use .\venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
python app.py
```

> The server should now be running at **[http://localhost:8000](http://localhost:8000)**.

---

### **3. Frontend Setup (Astro)**

Return to the project root and install frontend dependencies:

```bash
cd ..
npm install
```

Run the Astro dev server:

```bash
npm run dev
```

> The frontend should now be running at **[http://localhost:4321](http://localhost:4321)**.

---

### **4. Environment Variables**

Create a `.env` file in the `src/` directory:

```plaintext
OPENAI_API_KEY=your-openai-api-key
```

---

## 🚀 Usage

1. Open **[http://localhost:4321](http://localhost:4321)** in your browser.
2. Fill in the form to generate a scenario.
3. Click **Generate Scenario** to see the magic happen.

---

## 📂 File Structure

- **/src/app.py** - FastAPI server handling the AI logic.
- **/src/requirements.txt** - Python dependencies.
- **/src/pages/index.astro** - Main frontend UI.
- **/src/pages/api/generate.js** - API handler for communication between the frontend and backend.

---

## 🧹 Clean Up

When you're done, deactivate the virtual environment:

```bash
deactivate
```

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

--
