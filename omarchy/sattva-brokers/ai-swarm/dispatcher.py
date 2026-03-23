import asyncio
import os
import json
import ollama
import google.generativeai as genai

# Configure Cloud Agent (Google API)
# Ensure GOOGLE_API_KEY is exported in your environment
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    genai.configure(api_key=google_api_key)
    cloud_model = genai.GenerativeModel('gemini-pro')
else:
    print("Warning: GOOGLE_API_KEY not set. Cloud Strategist will fail.")

async def local_sentinel_agent(document_text, doc_type="COA"):
    """
    LLAMA 3 (Local) - Handles RED/AMBER Data.
    Extracts structured compliance data without data leaving Omarchy Linux.
    """
    print(f"[Llama 3] Analyzing {doc_type} (RED DATA)...")
    prompt = f"Extract the Max Moisture % and Lot ID from this {doc_type}. Return JSON only.\n\n{document_text}"
    
    # Non-blocking call to local Ollama
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    
    # In a production environment, we'd add JSON parsing/validation here
    return {"source": "llama3", "classification": "red_to_green", "data": response['message']['content']}

async def cloud_strategist_agent(sanitized_metrics):
    """
    GOOGLE API (Cloud) - Handles GREEN Data.
    Performs predictive analytics and supplier scoring based on sanitized inputs.
    """
    print("[Google API] Calculating Supplier Scorecard (GREEN DATA)...")
    prompt = f"Based on these sanitized metrics: {sanitized_metrics}, generate a supplier reliability score (1-100) and brief justification."
    
    # Non-blocking call to Google API
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, cloud_model.generate_content, prompt)
    return {"source": "google_api", "classification": "green_analytics", "data": response.text}

async def swarm_process_shipment(raw_coa_text):
    """
    Concurrent Swarm Execution: 
    1. Llama extracts data locally. 
    2. Passes sanitized data to Google API for strategic analysis.
    """
    print("--- Initiating Swarm Workflow ---")
    
    # Step 1: Local extraction (Secure)
    extracted_data = await local_sentinel_agent(raw_coa_text)
    print(f"[Orchestrator] Extracted Green Metrics: {extracted_data['data']}")
    
    # Step 2: Send sanitized metrics to Google API for strategic analysis
    cloud_task = asyncio.create_task(cloud_strategist_agent(extracted_data['data']))
    
    # Wait for cloud analysis to complete
    strategic_insight = await cloud_task
    
    print("--- Swarm Workflow Complete ---")
    return {
        "compliance_extraction": extracted_data,
        "strategic_analysis": strategic_insight
    }

if __name__ == "__main__":
    # Simulated Red Data (Raw Document) - e.g. from OCR or Nextcloud PDF text extraction
    sample_coa = "LOT: 2026-ONION-042. Moisture content detected at 11.5%. Pathogens: Negative."
    
    # Run the swarm execution
    results = asyncio.run(swarm_process_shipment(sample_coa))
    
    print("\n[Final Odoo Payload Ready for JSON-RPC via n8n]")
    print(json.dumps(results, indent=2))