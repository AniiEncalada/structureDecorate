package unl.cis.swem.creationalpatterns.decorator;

import unl.cis.swem.creationalpatterns.domain.Task;

public class PersonExtraHoursAndBonus extends PersonDecorator{
    public PersonExtraHoursAndBonus(Task task){
        super(task);
    }

    @Override
    public void tarea(){
        getTask().tarea();
        System.out.println("and I am working extra hours and I am getting a bonus");
    }
}
