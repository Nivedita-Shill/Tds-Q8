import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Analyst Email: 24f1001642@ds.study.iitm.ac.in

def main():
    # Data for 2024
    data = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'MRR_Growth': [1.34, 8.94, 9.63, 8.24]
    }
    df = pd.DataFrame(data)

    # Calculate Average
    current_avg = df['MRR_Growth'].mean()
    target = 15.0
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    plt.plot(df['Quarter'], df['MRR_Growth'], marker='o', label='Actual Growth', color='blue')
    plt.axhline(y=target, color='red', linestyle='--', label=f'Target ({target})')
    plt.axhline(y=current_avg, color='green', linestyle=':', label=f'Average ({current_avg:.2f})')
    
    plt.title('SaaS MRR Growth Analysis 2024')
    plt.ylabel('Growth (%)')
    plt.legend()
    plt.savefig('mrr_chart.png')
    print(f"Chart saved. Average Growth: {current_avg}")

if __name__ == "__main__":
    main()
