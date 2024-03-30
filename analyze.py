import pandas as pd
import nltk
nltk.download('stopwords') # stopwords is a list of common words that are usually filtered out in text processing, it is a file which needs to be downloaded if not already present
nltk.download('punkt') # punkt is a pre-trained model that helps in tokenizing the text into words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


def read_company_data(file_path):
    try:
        company_data = pd.read_csv(file_path)
        # Process the company data here
        return company_data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def read_student_data(file_path):
    try:
        student_data = pd.read_csv(file_path)
        # Process the student data here
        return student_data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def load_data():
    # Usage example
    company_data = read_company_data('company_data.csv')
    student_data = read_student_data('student_data.csv')
    return company_data, student_data

def most_common_word_job_description(company_data):
    # Extract the job_description column
    descriptions = company_data['job_description']

    # Tokenize the descriptions into words
    words = word_tokenize(" ".join(descriptions))

    # Filter out stop words
    stop_words = set(stopwords.words('english')).union(set([".", ","]))
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Count the frequency of the remaining words
    word_freq = Counter(filtered_words)

    # Display the most common words
    return word_freq.most_common(10)

# get_jobs_for_candidate takes all job_data and a single student_data
# and returns a list of jobs that are relevant to the student, if not tags
# match between student and job, return an empty list. It ranks the jobs
# based on the number of cs_language_tags that match between the student and 
# the cs_language_tags of the job. all
def get_jobs_for_candidate(job_data, student_data):
    relevant_jobs = []

    # Assuming each job data and student data has a 'cs_language_tags' field
    # which is a list of strings
    for job in job_data:
        print("job ", job)
        matching_tags = set(job['cs_language_tags']).intersection(student_data['cs_language_tags'])
        if matching_tags:
            # Add the job to the list along with the count of matching tags
            relevant_jobs.append((job, len(matching_tags)))

    # Sort the jobs in descending order of the count of matching tags
    relevant_jobs.sort(key=lambda x: x[1], reverse=True)

    # Return only the jobs, not the counts
    return [job for job, count in relevant_jobs]



if __name__ == "__main__":
    company_data, student_data = load_data()
    word_freq = most_common_word_job_description(company_data)
    print("most common words ", word_freq)
    for index, row in student_data.iterrows():
        sorted_jobs = get_jobs_for_candidate(company_data.to_dict('records'), row)
        print(f"Jobs relevant to student {row['id']}: {sorted_jobs}")
    