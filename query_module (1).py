def compute_average(values):
    # Manually calculate average
    return sum(values) / len(values) if values else 0

def compute_median(values):
    # Manually calculate median
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return 0
    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2

def compute_mode(values):
    # Manually calculate mode
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return modes[0] if modes else None

def compute_average(values):
    return sum(values) / len(values) if values else 0

def compute_median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return 0
    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2

def compute_mode(values):
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    max_count = max(freq.values()) if freq else 0
    modes = [k for k, v in freq.items() if v == max_count]
    return modes[0] if modes else None

def query_smokers_with_hypertension_and_stroke(data):
    ages = []

    for record in data.values():
        try:
            if (record["Smoking Status"].lower() != "never smoked" and
                record["Hypertension"] == "1" and
                record["Stroke Occurrence"] == "1"):
                age = int(record["Age"])
                ages.append(age)
        except:
            continue

    avg = compute_average(ages)
    med = compute_median(ages)
    mode = compute_mode(ages)

    result = {
        "Average Age": avg,
        "Median Age": med,
        "Mode Age": mode
    }

    # Save result to a CSV file
    with open("query_result_1.csv", "w") as f:
        f.write("Average Age,Median Age,Mode Age\\n")
        f.write(f"{avg},{med},{mode}\\n")

    return result



def query_heart_disease_with_stroke(data):
    ages = []
    glucose_levels = []

    for record in data.values():
        try:
            if record["Heart Disease"] == "1" and record["Stroke Occurrence"] == "1":
                ages.append(int(record["Age"]))
                glucose_levels.append(float(record["Average Glucose Level"]))
        except:
            continue

    avg_age = compute_average(ages)
    med_age = compute_median(ages)
    mode_age = compute_mode(ages)
    avg_glucose = compute_average(glucose_levels)

    result = {
        "Average Age": avg_age,
        "Median Age": med_age,
        "Mode Age": mode_age,
        "Average Glucose Level": avg_glucose
    }

    # Save result to a CSV file
    with open("query_result_2.csv", "w") as f:
        f.write("Average Age,Median Age,Mode Age,Average Glucose Level\n")
        f.write(f"{avg_age},{med_age},{mode_age},{avg_glucose}\n")

    return result


def query_gender_based_hypertension_stroke(data):
    groups = {
        "Male_Stroke": [],
        "Female_Stroke": [],
        "Male_No_Stroke": [],
        "Female_No_Stroke": []
    }

    for record in data.values():
        try:
            if record["Hypertension"] == "1":
                gender = record["Gender"].strip()
                age = int(record["Age"])
                had_stroke = record["Stroke Occurrence"] == "1"

                if gender == "Male" and had_stroke:
                    groups["Male_Stroke"].append(age)
                elif gender == "Female" and had_stroke:
                    groups["Female_Stroke"].append(age)
                elif gender == "Male":
                    groups["Male_No_Stroke"].append(age)
                elif gender == "Female":
                    groups["Female_No_Stroke"].append(age)
        except:
            continue

    result = {}

    for group_name, ages in groups.items():
        result[group_name] = {
            "Average Age": compute_average(ages),
            "Median Age": compute_median(ages),
            "Mode Age": compute_mode(ages)
        }

    # Save result to a CSV file
    with open("query_result_3.csv", "w") as f:
        f.write("Group,Average Age,Median Age,Mode Age\n")
        for group_name, stats in result.items():
            f.write(f"{group_name},{stats['Average Age']},{stats['Median Age']},{stats['Mode Age']}\n")

    return result


def query_smoking_and_stroke(data):
    with_stroke = []
    without_stroke = []

    for record in data.values():
        try:
            if record["Smoking Status"].lower() != "never smoked":
                age = int(record["Age"])
                if record["Stroke Occurrence"] == "1":
                    with_stroke.append(age)
                else:
                    without_stroke.append(age)
        except:
            continue

    result = {
        "Smokers With Stroke": {
            "Average Age": compute_average(with_stroke),
            "Median Age": compute_median(with_stroke),
            "Mode Age": compute_mode(with_stroke)
        },
        "Smokers Without Stroke": {
            "Average Age": compute_average(without_stroke),
            "Median Age": compute_median(without_stroke),
            "Mode Age": compute_mode(without_stroke)
        }
    }

    # Save to CSV
    with open("query_result_4.csv", "w") as f:
        f.write("Group,Average Age,Median Age,Mode Age\n")
        f.write(f"Smokers With Stroke,{result['Smokers With Stroke']['Average Age']},{result['Smokers With Stroke']['Median Age']},{result['Smokers With Stroke']['Mode Age']}\n")
        f.write(f"Smokers Without Stroke,{result['Smokers Without Stroke']['Average Age']},{result['Smokers Without Stroke']['Median Age']},{result['Smokers Without Stroke']['Mode Age']}\n")

    return result


def query_stroke_by_residence(data):
    urban_ages = []
    rural_ages = []

    for record in data.values():
        try:
            if record["Stroke Occurrence"] == "1":
                age = int(record["Age"])
                residence = record["Residence Type"].strip().lower()

                if residence == "urban":
                    urban_ages.append(age)
                elif residence == "rural":
                    rural_ages.append(age)
        except:
            continue

    result = {
        "Urban": {
            "Average Age": compute_average(urban_ages),
            "Median Age": compute_median(urban_ages),
            "Mode Age": compute_mode(urban_ages)
        },
        "Rural": {
            "Average Age": compute_average(rural_ages),
            "Median Age": compute_median(rural_ages),
            "Mode Age": compute_mode(rural_ages)
        }
    }

    # Save result to CSV
    with open("query_result_5.csv", "w") as f:
        f.write("Group,Average Age,Median Age,Mode Age\n")
        f.write(f"Urban,{result['Urban']['Average Age']},{result['Urban']['Median Age']},{result['Urban']['Mode Age']}\n")
        f.write(f"Rural,{result['Rural']['Average Age']},{result['Rural']['Median Age']},{result['Rural']['Mode Age']}\n")

    return result


def query_dietary_habits_by_stroke(data):
    with_stroke = {}
    without_stroke = {}

    for record in data.values():
        try:
            diet = record["Dietary Habits"].strip()
            stroke = record["Stroke Occurrence"]

            if stroke == "1":
                with_stroke[diet] = with_stroke.get(diet, 0) + 1
            elif stroke == "0":
                without_stroke[diet] = without_stroke.get(diet, 0) + 1
        except:
            continue

    # Save to CSV
    with open("query_result_6.csv", "w") as f:
        f.write("Dietary Habit,With Stroke Count,Without Stroke Count\n")

        all_habits = set(with_stroke.keys()) | set(without_stroke.keys())

        for habit in all_habits:
            count_with = with_stroke.get(habit, 0)
            count_without = without_stroke.get(habit, 0)
            f.write(f"{habit},{count_with},{count_without}\n")

    result = {
        "With Stroke": with_stroke,
        "Without Stroke": without_stroke
    }

    return result

def query_hypertension_with_stroke(data):
    result_records = []

    # Extract headers from any one sample record
    headers = list(next(iter(data.values())).keys())

    for record_id, record in data.items():
        try:
            if record["Hypertension"] == "1" and record["Stroke Occurrence"] == "1":
                row = [record_id] + [record[h] for h in headers]
                result_records.append(row)
        except:
            continue

    # Save to CSV
    with open("query_result_7.csv", "w") as f:
        f.write("ID," + ",".join(headers) + "\n")
        for row in result_records:
            f.write(",".join(row) + "\n")

    return result_records

def query_hypertension_stroke_split(data):
    with_stroke = []
    without_stroke = []

    headers = list(next(iter(data.values())).keys())

    for record_id, record in data.items():
        try:
            if record["Hypertension"] == "1":
                row = [record_id] + [record[h] for h in headers]
                if record["Stroke Occurrence"] == "1":
                    with_stroke.append(row)
                else:
                    without_stroke.append(row)
        except:
            continue

    # Save to CSV
    with open("query_result_8.csv", "w") as f:
        f.write("Group,ID," + ",".join(headers) + "\n")

        for row in with_stroke:
            f.write("With Stroke," + ",".join(row) + "\n")
        for row in without_stroke:
            f.write("Without Stroke," + ",".join(row) + "\n")

    return {
        "With Stroke": with_stroke,
        "Without Stroke": without_stroke
    }

def query_heart_disease_with_stroke_records(data):
    results = []
    headers = list(next(iter(data.values())).keys())

    for record_id, record in data.items():
        try:
            if record["Heart Disease"] == "1" and record["Stroke Occurrence"] == "1":
                row = [record_id] + [record[h] for h in headers]
                results.append(row)
        except:
            continue

    # Save to CSV
    with open("query_result_9.csv", "w") as f:
        f.write("ID," + ",".join(headers) + "\n")
        for row in results:
            f.write(",".join(row) + "\n")

    return results

def compute_std(values, mean):
    if not values:
        return 0
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5

def compute_percentile(values, percent):
    if not values:
        return 0
    values = sorted(values)
    k = (len(values) - 1) * percent
    f = int(k)
    c = k - f
    if f + 1 < len(values):
        return values[f] + c * (values[f + 1] - values[f])
    else:
        return values[f]

def descriptive_statistics(data, feature):
    values = []

    for record in data.values():
        try:
            val = float(record[feature])
            values.append(val)
        except:
            continue

    if not values:
        print("No valid numerical data found for that feature.")
        return {}

    mean = compute_average(values)
    std = compute_std(values, mean)
    min_val = min(values)
    max_val = max(values)
    p25 = compute_percentile(values, 0.25)
    p50 = compute_percentile(values, 0.50)
    p75 = compute_percentile(values, 0.75)

    result = {
        "Mean": mean,
        "Standard Deviation": std,
        "Min": min_val,
        "25%": p25,
        "50%": p50,
        "75%": p75,
        "Max": max_val
    }

    # Save to CSV
    with open("query_result_10.csv", "w") as f:
        f.write("Statistic,Value\n")
        for key, value in result.items():
            f.write(f"{key},{value}\n")

    return result


def query_average_sleep_by_stroke(data):
    with_stroke = []
    without_stroke = []

    for record in data.values():
        try:
            hours = float(record["Sleep Hours"])
            if record["Stroke Occurrence"] == "1":
                with_stroke.append(hours)
            elif record["Stroke Occurrence"] == "0":
                without_stroke.append(hours)
        except:
            continue

    avg_with = compute_average(with_stroke)
    avg_without = compute_average(without_stroke)

    result = {
        "Average Sleep Hours (With Stroke)": avg_with,
        "Average Sleep Hours (Without Stroke)": avg_without
    }

    # Save to CSV
    with open("query_result_11.csv", "w") as f:
        f.write("Group,Average Sleep Hours\n")
        f.write(f"With Stroke,{avg_with}\n")
        f.write(f"Without Stroke,{avg_without}\n")

    return result
 
