package sample;

import com.gluonhq.charm.glisten.control.TextField;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.ToggleButton;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Controller {

    @FXML
    private TextField District_Input;
    @FXML
    private TextArea Predictions, AboutText;
    @FXML
    private ToggleButton Trainer;
    @FXML
    private ToggleButton Show_Me;
    @FXML
    private WebView Map_Plot;
    @FXML
    private Button OK;


    String Output = null;

    public void run() {
        try {
            int validator = 0;
            int validator1 = 0 ;
            if(Trainer.isSelected())
            {
                validator = 1;
            }
            if(Show_Me.isSelected())
            {
                validator1 = 1;
            }
            Process process = Runtime.getRuntime().exec("python -u D:\\Personal_Projects\\Python\\DTLAB\\DTLAB.py " + District_Input.getText() + " " + validator + " " + validator1);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(process.getInputStream()));
            Predictions.appendText("The Land is ");
            while ((Output = stdInput.readLine()) != null) {
                Predictions.appendText(Output + "\n");
            }


        }
        catch (IOException Text) {
            System.out.print(Text);
        }
    }

    public void plot()
    {
        try
        {
            WebEngine WE = Map_Plot.getEngine();
            Map_Plot.setZoom(.85);
            WE.load("https://www.google.com/maps/place/" + District_Input.getText());
        }
        catch(Exception e)
        {
                System.out.println(e);
        }
    }

    public void exit()
    {

        System.exit(0);
    }

    public void reset()
    {
        District_Input.setText("");
    }

    public void About()
    {
        AboutText.setStyle("-fx-opacity: 1.0");
        OK.setStyle("-fx-opacity: 1.0");
    }

    public void hide()
    {
        AboutText.setStyle("-fx-opacity: 0.0");
        OK.setStyle("-fx-opacity: 0.0");
    }



}
