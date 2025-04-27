from dataset_module import load_dataset
import query_module as queries

def show_menu():
    print("\n=== Stroke Data Analysis Menu ===")
    print("1. Smokers + Hypertension + Stroke Analysis")
    print("2. Heart Disease and Stroke")
    print("3. Gender-wise Hypertension and Stroke")
    print("4. Smoking Habits Comparison")
    print("5. Residence (Urban/Rural) Stroke Cases")
    print("6. Dietary Habits (Stroke vs No Stroke)")
    print("7. Hypertension Resulted in Stroke")
    print("8. Hypertension Patients: Stroke vs No Stroke")
    print("9. Full Records: Heart Disease and Stroke")
    print("10. Descriptive Stats for Selected Feature")
    print("11. Sleep Hours Comparison (Stroke/No Stroke)")
    print("0. Exit")

def run_ui():
    print(">> Loading the stroke dataset...")
    file_name = "data.csv" 
    data_dict = load_dataset(file_name)

    if not data_dict:
        print("!! Couldn't load dataset. Exiting...")
        return

    print(" Dataset loaded successfully. Ready to analyze!")

    while True:
        show_menu()
        user_choice = input("Pick a query number (or 0 to quit): ").strip()

        if user_choice == "0":
            print(" Thanks for using Stroke Analysis System. Bye!")
            break

        try:
            if user_choice == "1":
                print("\n[Running Query 1]")
                print(queries.query_smokers_with_hypertension_and_stroke(data_dict))
            elif user_choice == "2":
                print("\n[Running Query 2]")
                print(queries.query_heart_disease_with_stroke(data_dict))
            elif user_choice == "3":
                print("\n[Running Query 3]")
                result = queries.query_gender_based_hypertension_stroke(data_dict)
                for group, details in result.items():
                    print(group, details)
            elif user_choice == "4":
                print("\n[Running Query 4]")
                print(queries.query_smoking_and_stroke(data_dict))
            elif user_choice == "5":
                print("\n[Running Query 5]")
                print(queries.query_stroke_by_residence(data_dict))
            elif user_choice == "6":
                print("\n[Running Query 6]")
                result = queries.query_dietary_habits_by_stroke(data_dict)
                print("Patients with Stroke:", result["With Stroke"])
                print("Patients without Stroke:", result["Without Stroke"])
            elif user_choice == "7":
                print("\n[Running Query 7]")
                records = queries.query_hypertension_with_stroke(data_dict)
                print(f"Total Patients Found: {len(records)}")
            elif user_choice == "8":
                print("\n[Running Query 8]")
                groups = queries.query_hypertension_stroke_split(data_dict)
                print(f"Hypertension + Stroke: {len(groups['With Stroke'])}")
                print(f"Hypertension + No Stroke: {len(groups['Without Stroke'])}")
            elif user_choice == "9":
                print("\n[Running Query 9]")
                full_records = queries.query_heart_disease_with_stroke_records(data_dict)
                print(f"Full Records Found: {len(full_records)}")
            elif user_choice == "10":
                print("\n[Running Query 10]")
                feature_name = input("Enter the feature/column you want stats for: ").strip()
                print(queries.descriptive_statistics(data_dict, feature_name))
            elif user_choice == "11":
                print("\n[Running Query 11]")
                print(queries.query_average_sleep_by_stroke(data_dict))
            else:
                print(" Invalid choice. Please select a valid number from the menu!")

        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
            

