import re


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    investments = []
    current_user = None
    current_institution = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match usuário/instituição
        user_match = re.match(r'(\w+)\s+(\w+)', line)
        if user_match:
            current_user = user_match.group(1)
            current_institution = user_match.group(2)
            continue

        # Match título
        title_match = re.match(r'([\w\s\.]+)\s+(\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)\s+(\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)\s+([\-]?\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)', line)
        if title_match and current_user and current_institution:
            name = title_match.group(1).strip()
            value_str = title_match.group(2).replace('.', '').replace(',', '.')
            prev_str = title_match.group(3).replace('.', '').replace(',', '.')
            gain_str = title_match.group(4).replace('.', '').replace(',', '.')

            investments.append({
                "user": current_user,
                "institution": current_institution,
                "name": name,
                "value": float(value_str),
                "previous_value": float(prev_str),
                "gain": float(gain_str),
                "gain_percent": (float(gain_str) / float(prev_str)) * 100 if float(prev_str) != 0 else 0
            })

    return investments