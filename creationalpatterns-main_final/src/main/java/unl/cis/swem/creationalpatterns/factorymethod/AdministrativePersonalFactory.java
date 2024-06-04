/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package unl.cis.swem.creationalpatterns.factorymethod;

import java.time.LocalDate;
import java.time.Month;
import unl.cis.swem.creationalpatterns.domain.Person;
import unl.cis.swem.creationalpatterns.domain.AdministrativePersonal;

/**
 *
 * @author wduck
 */
public class AdministrativePersonalFactory extends PersonFactoryMethod{

    @Override
    public Person create() {
        AdministrativePersonal object = (AdministrativePersonal)dataIngress(); 
        return object;
    }

    @Override
    public Person dataIngress() {
        // AquI INGRESAR INFO
        LocalDate now = LocalDate.of(2001, Month.JULY, 30);
        AdministrativePersonal s = new AdministrativePersonal("Kimberly", "Flores del Jardín", "110456980", now, "Director");
        return s;
    }
}
