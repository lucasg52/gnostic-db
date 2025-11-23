from keyword_extractor.extract_keywords_to_json import extract_keywords_to_json
import json
import os

if __name__ == "__main__":
    # Load test cases from JSON file
    test_cases_file = "test_cases.json"
    
    if not os.path.exists(test_cases_file):
        print(f"Error: {test_cases_file} not found!")
        exit(1)
    
    with open(test_cases_file, "r", encoding="utf-8") as f:
        test_data = json.load(f)
    
    test_cases = test_data.get("test_cases", [])
    
    if not test_cases:
        print("No test cases found in JSON file!")
        exit(1)
    
    print(f"Running {len(test_cases)} test cases...\n")
    print("=" * 80)
    
    # Create output directory for results
    output_dir = "test_outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run each test case
    for i, test_case in enumerate(test_cases, 1):
        name = test_case.get("name", f"Test {i}")
        title = test_case.get("title", "")
        paragraph = test_case.get("paragraph", "")
        
        print(f"\n[{i}/{len(test_cases)}] Test: {name}")
        print(f"Title: {title}")
        print("-" * 80)
        
        # Generate output filename
        safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name)
        output_file = os.path.join(output_dir, f"{safe_name.lower().replace(' ', '_')}_keywords.json")
        
        try:
            # Extract keywords
            keywords = extract_keywords_to_json(title, paragraph, output_file=output_file)
            
            # Load and display results
            with open(output_file, "r", encoding="utf-8") as f:
                result = json.load(f)
            
            print(f"\nExtracted {len(result)} keywords:")
            for j, kw in enumerate(result, 1):
                print(f"  {j}. {kw}")
            
            print(f"\nResults saved to: {output_file}")
            
        except Exception as e:
            print(f"ERROR: {str(e)}")
        
        print("=" * 80)
    
    print(f"\nAll tests completed! Results saved in '{output_dir}/' directory.")
    