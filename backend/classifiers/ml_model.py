def classify_file(file_path):
    # Placeholder for ML classification logic
    extension = file_path.split('.')[-1].lower()
    if extension in ['jpg', 'png', 'jpeg']:
        return "Image"
    elif extension in ['pdf', 'docx', 'txt']:
        return "Document"
    else:
        return "Other"
