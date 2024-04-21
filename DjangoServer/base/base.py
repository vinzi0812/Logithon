import google.generativeai as genai

def get_user_input():
    mode_of_travel = "air"
    is_transhipment = input("Is this a transhipment? (Yes/No): ").lower()
    stopages = []
    if is_transhipment == "yes":
        num_stopages = int(input("Enter the number of stopages: "))
        for i in range(num_stopages):
            stopages.append(input(f"Enter stopage {i+1}: "))
    return mode_of_travel, is_transhipment, stopages

def create_gemini_prompt(source, destination, mode_of_travel, is_transhipment, stopages):
    prompt = f"Find the 5 best routes for shipping from {source} to {destination} by {mode_of_travel} mode, optimized for time, cost, and fuel consumption. "
    
    if is_transhipment == "yes":
        prompt += "This is a transhipment with the following stopages: "
        for stopage in stopages:
            prompt += f"{stopage}, "
        prompt = prompt.rstrip(", ")  # Remove the trailing comma and space
    
    prompt += ". Clearly divide and bifurcate the journey into various laps according to the mode of travel, and provide accurate information on all ports, airports, cities, and areas in transit. Your answer should be strictly just a list of dictionaries, each consisting of the following: 'source', 'destination', 'laps' which will be again a list of dictionaries containing 'start place', 'end place', 'distance', 'duration', 'fuel consumption', 'cost'. Finally each route will have a 'total distance', 'total duration', 'total fuel consumption', 'total cost'. Think of it like you are giving me a python dictionary"
    
    return prompt

def generate_gemini_prompt(prompt):
    genai.configure(api_key="AIzaSyA181AEFg-9i8m0I7QwcrGdA4dw7SlGvjo")
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    gemini_prompt = convo.last.text
    return gemini_prompt

def airmain(source, destination):
    mode_of_travel, is_transhipment, stopages = get_user_input()
    initial_prompt = create_gemini_prompt(source, destination, mode_of_travel, is_transhipment, stopages)
    gemini_prompt = generate_gemini_prompt(initial_prompt)
    print("\nGemini API Prompt:")
    print(gemini_prompt)

if __name__ == "__main__":
    airmain("New York", "Mumbai")