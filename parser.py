from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template=(
    "You are tasked with extracting specific information from the following text content: {dom_content}\n\n"
    "Please follow these instructions :\n\n"
    "1.**Extract Information:** Only extract the informaation that directly matches the provided description: {parse_description}."
    "2.**No Extra Content:** Do not include any additional text,comments or explanations in your response."
    
    "3.**Empty Response:** If no information matches the description, return an empty string('')"
    "4.**Direct Data only:** Your output should contain only the data explicitly requested, with no other"

)
model= OllamaLLM(model="llama3")

def parse_with_ollama(dom_chunks,parse_description):
    prompt=ChatPromptTemplate.from_template(template)
    chain=prompt | model
    parsed_results=[]
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    for i ,chunk in enumerate(dom_chunks,start=1):
        response=chain.invoke(
            {"dom_content":chunk,"parse_description":parse_description}

        )
        print(f"Parsed batch{i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)