# SpeakSynk Flow Processor


Parent class to create steps, ideally this will save us some common functions of the steps.


# Implementation


```
from speaksynk_flow_processor.AWSSpeakSynkFlowProcesor import AWSSpeakSynkFlowProcesor

class SomeStep(AWSSpeakSynkFlowProcesor):
    def run(self):
        super().run()
        # Some logic


if __name__ == '__main__':
    step = SomeSteP()
    step.download()
    step.run()
    step.upload('hestep/%s' %s self._identifier)  
    
```

Ideally this save us some time in creating more steps and only taking care of the run method


# Install

* `pip install poetry`
* `poetry install`

# Test

* `poetry run pytest`


# Use

* `poetry run python xxxx`