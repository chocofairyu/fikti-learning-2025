import json

with open('/vercel/sandbox/uploads/projek-capstone (2).ipynb') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        code = cell['source']
        if isinstance(code, list):
            code = ''.join(code)
        try:
            compile(code, f'cell_{i}', 'exec')
            print(f"Cell {i}: OK")
        except SyntaxError as e:
            print(f"Cell {i}: Syntax Error - {e}")