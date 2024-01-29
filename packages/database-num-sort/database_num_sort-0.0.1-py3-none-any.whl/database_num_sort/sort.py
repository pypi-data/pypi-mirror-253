import sqlite3

def sort(database_name, table_name, column_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # 获取所有行的 uid
    cursor.execute(f'SELECT {column_name} FROM {table_name}')
    all_uids = [row[0] for row in cursor.fetchall()]
    # 找到 uid 中的间断数字
    gaps = [uid for uid in range(1, max(all_uids)) if uid not in all_uids]
    # 将间断数字后的行的 uid 减一
    for gap in gaps:
        cursor.execute(f'UPDATE {table_name} SET {column_name}=? WHERE {column_name} > ?', (gap, gap))
    conn.commit()
    conn.close()
    return gaps
