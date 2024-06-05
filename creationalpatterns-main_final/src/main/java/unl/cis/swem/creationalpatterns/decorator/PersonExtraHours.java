package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public class PersonExtraHours extends PersonDecorator{
    public PersonExtraHours(Task task){
        super(task);
    }

    @Override
    public void tarea(){
        getTask().tarea();
        System.out.println("and I am working extra hours");
    }
}
