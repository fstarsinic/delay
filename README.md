# delay
A module to calculate smarter delays. 
- This can be used for alerts and alarms to avoid alarm fatigue. 
- This can be used to calculate subsequent wait times before re-trying a function that might take an unknown amount of time to complete.
---
The module uses the fibonacci sequence to determine the delay increase. A delay factor can also be used to increase the delay by a multiple, at creation time.
---
**Example**
>
    a = Delay(1) #Start with a delay of 1
    while True:
      result = run_some_function()
      if not result:
        new_delay = a.increase_delay()
        time.sleep(new_delay)
      else:
        save_results(result)
        break
