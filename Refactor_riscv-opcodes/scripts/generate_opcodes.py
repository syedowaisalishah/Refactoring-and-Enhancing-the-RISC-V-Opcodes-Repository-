import yaml
import os

def load_instructions(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_opcodes(instructions):
    opcodes = []
    for instruction in instructions:
        opcodes.append(f"{instruction['name']} {instruction['format']}")
    return opcodes

def write_opcodes(opcodes, output_path):
    with open(output_path, 'w') as file:
        for opcode in opcodes:
            file.write(opcode + '\n')

if __name__ == "__main__":
    modules = ['rv_i', 'rv_a']
    for module in modules:
        instructions = load_instructions(f'modules/{module}.yaml')['instructions']
        opcodes = generate_opcodes(instructions)
        write_opcodes(opcodes, module)
