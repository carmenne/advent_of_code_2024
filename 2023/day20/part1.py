commands = {}
modules = {}
broadcaster = ()
with open("input_long.txt", "r") as file:
    for line in file:
        ins, outs = line.strip().split("->")
        module = ins.strip().replace("%", "").replace("&", "")
        command = [o.strip() for o in outs.strip().split(",")]
        if module == "broadcaster":
            broadcaster = command
        else:
            module_type = ins.strip()[:1]
            modules[module] = (module_type, "OFF") if module_type == "%" else (module_type, {})
            commands[module] = command

for module in modules.keys():
    if modules[module][0] == "&":
        for k, v in commands.items():
            if module in v:
                modules[module][1][k] = "low"


def can_propagate(type, sender):
    if sender == "broadcaster":
        return 1, 0, "low"

    if modules[sender][0] == "%":
        if type == "high":
            return 0, 0, "ignore"
        else:
            if modules[sender][1] == "OFF":
                return 0, 1, "high"
            else:
                return 1, 0, "low"
    else:
        inputs = list(modules[sender][1].values())
        if inputs.count("high") == len(inputs):
            return 1, 0, "low"
        else:
            return 0, 1, "high"


t_l, t_h = 0, 0
TIMES = 1000

for push in range(TIMES):
    queue = []
    t_l += 1
    for m in broadcaster:
        queue.append(("low", "broadcaster", m))

    while queue:
        type, sender, receiver = queue.pop(0)

        if type == "update":
            modules[sender] = receiver
            continue

        new_low, new_high, new_type = can_propagate(type, sender)
        if receiver in modules and modules[receiver][0] == "&":
            if new_type != "ignore":
                modules[receiver][1][sender] = new_type

        if new_low == 0 and new_high == 0:
            continue

        t_l, t_h = t_l + new_low, t_h + new_high

        new_receivers = commands[receiver] if receiver in commands else []
        i = 0
        for new_receiver in new_receivers:
            new_command = (new_type, receiver, new_receiver)
            queue.append(new_command)
            i += 1

        if sender in modules and modules[sender][0] == "%":
            queue.append(("update", sender, ("%","OFF") if modules[sender][1] == "ON" else ("%","ON")))

print(t_l, t_h, t_l * t_h) # 18806 * 47849 = 899848294
