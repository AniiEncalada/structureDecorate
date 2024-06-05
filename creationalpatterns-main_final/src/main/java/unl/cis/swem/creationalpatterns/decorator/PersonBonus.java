package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public class PersonBonus extends PersonDecorator{
    public PersonBonus(Task task){
        super(task);
    }

    @Override
    public void tarea(){
        getTask().tarea();
        System.out.println("and I am getting a bonus");
    }
}
