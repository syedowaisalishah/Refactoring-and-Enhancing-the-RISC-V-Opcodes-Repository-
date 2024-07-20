import yaml

def load_instructions(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_opcodes(instructions):
    opcodes = []
    for instruction in instructions:
        if instruction.get('pseudo_op', False):
            opcodes.append(f"$pseudo_op rv_i::{instruction['name']} {instruction['format']}")
        else:
            opcodes.append(f"{instruction['name']} {instruction['format']}")
    return opcodes

def write_opcodes(opcodes, output_path):
    with open(output_path, 'w') as file:
        for opcode in opcodes:
            file.write(opcode + '\n')

if __name__ == "__main__":
    instructions = load_instructions('modules/rv_i.yaml')['instructions']
    opcodes = generate_opcodes(instructions)
    write_opcodes(opcodes, 'rv_i')
