import csv
import os

""" CREATES THE CSV FOR MACHINE LEARNING """

#input_dir for dataset
input_dir = '../SeniorExperience/ReshapedImages'
csv_file = "../SeniorExperience/API/config/api/backend/handwriting_dataset.csv" 
data = []

for file_name in os.listdir(input_dir):
    if file_name.endswith(".png"):
        # extract the writer id from the file name and convert to integer 
        writer_id = int(file_name.split("_")[0][1:])
        prompt = file_name.split("_")[2][1:]
        image_path = os.path.join(input_dir, file_name)

        data.append([writer_id, prompt, image_path])
        print("WRITER: " + str(writer_id) + ", PROMPT: " + str(prompt))

print(data)

with open(csv_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["wid", "prompt" ,"image_path"])
    writer.writerows(data)