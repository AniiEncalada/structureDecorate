package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public abstract class PersonDecorator implements Task{
    private Task task;

    public PersonDecorator(Task task){
        this.task = task;
    }

    protected Task getTask(){
        return task;
    }
}
