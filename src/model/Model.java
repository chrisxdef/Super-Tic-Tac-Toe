package model;

import controller.Data;
import controller.Input;

/**
 * Created by lapost48 on 12/14/2016.
 */
public interface Model {

    public Data getData();

    public void update(Input input, boolean turn);

}
