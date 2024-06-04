package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public class PersonFeature extends PersonDecorator{
    public PersonFeature(Task task){
        super(task);
    }

    @Override
    public void tarea(){
        System.out.println("I am a person with a feature");
        getTask().tarea();
    }
}
