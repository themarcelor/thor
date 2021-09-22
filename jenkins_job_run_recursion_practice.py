from collections import OrderedDict


def step1_func():
    print("running step 1 function")


def step2_func():
    print("running step 2 function")


def step3_func():
    print("running step 3 function")


def step4_func():
    print("running step 4 function")


od = OrderedDict()

od["step1"] = {"run_next": "step2", "name": "step1", "func_ref": step1_func}
od["step2"] = {"run_next": "step3", "name": "step2", "func_ref": step2_func}
od["step3"] = {"run_next": "step4", "name": "step3", "func_ref": step3_func}
od["step4"] = {"name": "step4", "func_ref": step4_func}


def recursive_run_job(step_deets):
    result = step_deets["func_ref"]()
    if "run_next" in step_deets:
        recursive_run_job(od[step_deets["run_next"]])
    else:
        print(
            "this step does not have a 'run_next' property. So there is nothing left to do."
        )


recursive_run_job(od["step1"])
