"""Prepare synthetic survey data only in the isolated SUT runtime database."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / '.git' / 'sut-runtime' / 'database.sqlite'

if not DB.is_file():
    raise SystemExit('Start the isolated backend first; original SUT database is never used.')

with sqlite3.connect(DB) as connection:
    user_id = connection.execute('SELECT id FROM users WHERE email = ?', ('test@eshop.com',)).fetchone()[0]
    existing = connection.execute('SELECT count(*) FROM orders WHERE user_id = ?', (user_id,)).fetchone()[0]
    if existing:
        raise SystemExit('Survey account already has orders; refusing to overwrite them.')
    connection.execute('UPDATE users SET phone = ?, shipping_address = ? WHERE id = ?',
                       ('0912345678', '123 Đường Thử Nghiệm, Phường Mẫu', user_id))
    for index, status in enumerate(('pending', 'confirmed', 'shipping', 'delivered', 'canceled'), 1):
        connection.execute('INSERT INTO orders (user_id, total_amount, status, shipping_address, created_at) VALUES (?, ?, ?, ?, ?)',
                           (user_id, index * 1234567, status, 'Địa chỉ giả phục vụ khảo sát', f'2026-11-0{index} 08:15:00'))
    # A different account's row supports later ownership checks; not a completed test.
    connection.execute('INSERT INTO orders (user_id, total_amount, status, shipping_address) VALUES (?, ?, ?, ?)',
                       (1, 987654321, 'pending', 'Đơn của tài khoản khác — dữ liệu giả'))
print('Prepared five synthetic status examples for Test User and one other-account order.')
