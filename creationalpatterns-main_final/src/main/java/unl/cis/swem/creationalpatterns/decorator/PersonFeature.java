package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public class PersonFeature extends PersonDecorator{
    public PersonFeature(Task task){
        super(task);
    }

    @Override
    public void tarea(){
        getTask().tarea();
        System.out.println("and I am a person with a feature");
    }
}
