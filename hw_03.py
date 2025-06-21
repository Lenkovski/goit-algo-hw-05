import sys
import os

def parse_log_line(line: str) -> dict:
   
    parts = line.strip().split(' ', 3)  # розбиваємо на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level.upper(),  # робимо рівень у верхньому регістрі для уніфікації
        'message': message
    }

def load_logs(file_path: str) -> list:
  
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    
    level = level.upper()
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
 
    counts = {}
    for log in logs:
        lvl = log['level']
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

def display_log_counts(counts: dict):
  
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print('-' * 17 + '-|-' + '-' * 8)
    # Виводимо за алфавітом рівнів для порядку
    for level in sorted(counts.keys()):
        print(f"{level:<17} | {counts[level]:<8}")

def display_logs_details(logs: list, level: str):
    
    if not logs:
        print(f"Деталей для рівня '{level.upper()}' не знайдено.")
        return
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        print("Лог-файл порожній або не містить коректних записів.")
        sys.exit(0)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_logs_details(filtered_logs, level_filter)

if __name__ == "__main__":
    main()