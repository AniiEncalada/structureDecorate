/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package unl.cis.swem.creationalpatterns.factorymethod;

import unl.cis.swem.creationalpatterns.domain.Person;

/**
 *
 * @author wduck
 */
public abstract class PersonFactoryMethod implements Inable{
    
    public abstract Person create();
}
