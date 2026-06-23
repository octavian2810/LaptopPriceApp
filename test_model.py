import zipfile

try:
    with zipfile.ZipFile("models/ann_model.keras", "r") as z:
        print("Model valid")
        print(z.namelist())
except Exception as e:
    print("Error:", e)