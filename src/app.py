from fastapi import FastAPI, Request
from agents import Agent, Runner
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from openai import OpenAI
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# define agent
task_generator = Agent(
    name="AI Scenario Maker",
    instructions="""
## Scenario Generation Prompt for AI Image, Video, and Image-to-Video Creation  

### Objective  
Generate creative, visually rich scenarios based on the specified mode, output format, and specific subject. Focus exclusively on elements that can be clearly seen. Avoid non-visual descriptions like sound, smell, or abstract feelings unless they have a visible physical manifestation.  

---

### Instructions  

Generate a scenario based on the following parameters:  

#### 1. Scenario Type  
Choose one:  
- **Normal (default)** – Balanced storytelling for versatile use.  
- **Text to Image (t2i)** – Single-frame, visually rich prompts.  
- **Text to Video (t2v)** – Emphasizes motion, transitions, and evolving scenes.  
- **Image to Video (i2v)** – Extends a static image into a dynamic scene.  
- **Wan (t2v/i2v)** – Highly cinematic, director-like sequences with intense detail.  

#### 2. Output Format  
Choose one:  
- **Normal Version (default)** – Full sentences, immersive and context-rich.  
- **Tag Version** – Comma-separated key elements for concise control.  

#### 3. Custom Options (Optional)  
- **Token Limit Control** – Define the maximum and minimum token count (e.g., 60 to 150 tokens).  
- **Atmosphere, Lighting, and Style Control** – Specify the desired mood, lighting, and artistic style.  

#### 4. Scenario Description  
Describe the specific subject or theme for the scenario. Be clear about the setting, characters, or scene style to guide the generation process.  

---

### Visual-Only Focus  
Ensure the output focuses only on physical, visible elements. Avoid:  
- Abstract concepts (e.g., "magical ambience")  
- Purely internal states (e.g., "nervous energy")  
- Sounds or smells unless they have a visible impact (e.g., steam rising, vibrating glass)  

---

### Example Input  
- **Scenario Type:** t2i  
- **Output Format:** Normal Version  
- **Token Limit Control:** 150 max, 60 min  
- **Scenario:** Schoolgirl in a classroom, cyberpunk style  

### Example Output  
In a dimly lit classroom filled with neon-lit desks and holographic displays flickering with complex equations, a schoolgirl sits at the forefront. Her uniform, a futuristic blend of metallic fabrics and glowing circuits, shimmers with every slight movement. Her hair, an iridescent blend of blues and purples, cascades down to her shoulders, reflecting the pulsing lights of the room. Transparent data screens hover in front of each student, displaying interactive learning modules. Outside the window, the skyline of a sprawling cyberpunk city glows with luminous skyscrapers and floating traffic.  

### Example Tag Version  
Schoolgirl, neon-lit classroom, holographic displays, futuristic uniform, glowing circuits, iridescent hair, data screens, cyberpunk city skyline, floating traffic.  

---

### Tips for Best Results  
- Focus on clear, concrete visuals.  
- Avoid referencing sound, smell, or purely abstract emotions.  
- Be specific with the scenario description to set a clear creative direction.  
- Use physical cues to imply atmosphere without relying on non-visual concepts.  

""",
)

# Generate the text prompt
async def generate_tasks(final_prompt):
    result = await Runner.run(task_generator, final_prompt)
    return result.final_output

# Generate the image based on the generated text prompt
async def generate_image(prompt):
    client = OpenAI(api_key=api_key)
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt
    )

    # Extract the base64 encoded image data
    image_base64 = result.data[0].b64_json
    return image_base64

@app.post("/generate")
async def generate(request: Request):
    try:
        # Extract the prompt data from the request
        data = await request.json()
        final_prompt = f"""
        - **Scenario Type**: {data['scenario_type']}
        - **Output format**: {data['output_type']} version
        - **Token Limit Control**: {data['max_tokens']} max, {data['min_tokens']} min
        - **Scenario**: {data['scenario']}
        """
        
        # Generate the text prompt
        text_prompt = await generate_tasks(final_prompt)

        # Generate the image using the generated text prompt
        image_base64 = await generate_image(text_prompt)

        # Return both the text and the image
        return JSONResponse({"output": text_prompt, "image": image_base64})

    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse({"error": "Failed to generate scenario."}, status_code=500)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)