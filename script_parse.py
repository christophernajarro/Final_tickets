import re
from datetime import datetime

def parse_logs(log_file, start_date, end_date, endpoint):
    """
    Parse a log file and count successes and failures for a specific endpoint within a date range.

    Args:
        log_file (str): Path to the log file.
        start_date (str): Start date in "YYYY-MM-DD" format.
        end_date (str): End date in "YYYY-MM-DD" format.
        endpoint (str): Endpoint to analyze, e.g., "/tickets/".

    Returns:
        dict: Dictionary with counts of successes and failures.
    """
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Pattern to match log entries
    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).* (?P<level>INFO|ERROR):(?P<message>.*Éxito en Ejecución|.*Error en Ejecución:.*)'
    )

    # Initialize counters
    success_count = 0
    failure_count = 0

    # Open and process the log file
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                log_data = match.groupdict()
                log_date = datetime.strptime(log_data["timestamp"], "%Y-%m-%d %H:%M:%S")
                log_message = log_data["message"]

                # Filter by date range
                if start_date <= log_date <= end_date:
                    if "Éxito en Ejecución" in log_message:
                        success_count += 1
                    elif "Error en Ejecución" in log_message:
                        failure_count += 1

    return {"success": success_count, "failure": failure_count}

# Example usage
if __name__ == "__main__":
    log_file = r"D:\Software\Examen final\logs\log_04_12_2024.log"  # Updated with the actual path
    start_date = "2024-12-01"
    end_date = "2024-12-05"
    endpoint = "/tickets/"

    result = parse_logs(log_file, start_date, end_date, endpoint)
    print(f"Results for endpoint {endpoint}:")
    print(f"Successes: {result['success']}")
    print(f"Failures: {result['failure']}")
