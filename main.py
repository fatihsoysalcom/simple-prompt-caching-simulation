import time
import hashlib

# Simple in-memory cache for demonstration purposes
prompt_cache = {}
cache_hits = 0
cache_misses = 0

def simulate_llm_response(prompt: str) -> str:
    """
    Simulates a time-consuming LLM API call.
    In a real scenario, this would be an actual API request to an LLM.
    """
    print(f"  [LLM] Processing new prompt: '{prompt}'...")
    time.sleep(1.5)  # Simulate network latency and processing time
    response = f"Response for '{prompt}' (generated at {time.strftime('%H:%M:%S')})"
    print(f"  [LLM] Finished processing for '{prompt}'.")
    return response

def get_llm_response_cached(prompt: str) -> str:
    """
    Retrieves an LLM response, utilizing a cache.
    If the prompt is in the cache, it returns the cached response instantly.
    Otherwise, it calls the simulated LLM, caches the result, and returns it.
    """
    global cache_hits, cache_misses

    # Using the prompt directly as the cache key for simplicity.
    # For very long prompts or security, a hash (e.g., hashlib.sha256) would be better.
    cache_key = prompt

    if cache_key in prompt_cache:
        # --- PROMPT CACHING DEMONSTRATION: CACHE HIT ---
        cache_hits += 1
        print(f"✅ Cache Hit for prompt: '{prompt}'")
        return prompt_cache[cache_key]
    else:
        # --- PROMPT CACHING DEMONSTRATION: CACHE MISS ---
        cache_misses += 1
        print(f"❌ Cache Miss for prompt: '{prompt}'. Calling LLM...")
        response = simulate_llm_response(prompt)
        prompt_cache[cache_key] = response # Store the new response in the cache
        return response

if __name__ == "__main__":
    print("--- Prompt Caching Simulation Start ---")
    print("This example simulates an LLM API call with a delay to show caching benefits.\n")

    prompts_to_test = [
        "What is prompt caching?",
        "Explain prompt caching in simple terms.",
        "What is prompt caching?", # Repeat to demonstrate cache hit
        "How does prompt caching improve performance?",
        "Explain prompt caching in simple terms.", # Repeat to demonstrate cache hit
        "Give me an example of a cache hit.",
        "What is prompt caching?", # Repeat again
    ]

    for i, prompt in enumerate(prompts_to_test):
        print(f"\n--- Query {i+1}/{len(prompts_to_test)} ---")
        start_time = time.perf_counter()
        response = get_llm_response_cached(prompt)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Response: {response}")
        print(f"Query took: {duration:.2f} seconds")

    print("\n--- Simulation Summary ---")
    print(f"Total Cache Hits: {cache_hits}")
    print(f"Total Cache Misses: {cache_misses}")
    print(f"Total Queries: {cache_hits + cache_misses}")
    print("\n--- Prompt Caching Simulation End ---")
