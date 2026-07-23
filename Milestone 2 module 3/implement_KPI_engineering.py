import pandas as pd

# Load dataset
df = pd.read_csv('final dataset university_cleaned.csv')

print("Columns:", df.columns.tolist())
print("\nShape:", df.shape)
print("\nHead:")
print(df.head())
print("\nInfo:")
print(df.info())
total_universities = df['university_name'].nunique()
avg_overall_score = df['overall_score'].mean()
avg_research_score = df['research_output_score'].mean()
total_countries = df['country'].nunique()

print(f"Total Unique Universities: {total_universities}")
print(f"Average Overall Score: {avg_overall_score:.2f}")
print(f"Average Research Output Score: {avg_research_score:.2f}")
print(f"Number of Countries: {total_countries}")
# Just getting a bit more context for a rounded response
summary_df = df[['overall_score', 'research_output_score']].describe()
print(summary_df)


# Check available relevant columns
cols = [
    'world_rank', 
    'citations_score', 
    'faculty_to_student_ratio', 
    'international_student_ratio', 
    'academic_reputation_score', 
    'research_productivity_index'
]

kpis = {}
for col in cols:
    if col in df.columns:
        kpis[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'min': df[col].min(),
            'max': df[col].max()
        }

for k, v in kpis.items():
    print(f"{k}: Mean={v['mean']:.2f}, Median={v['median']:.2f}, Min={v['min']:.2f}, Max={v['max']:.2f}")