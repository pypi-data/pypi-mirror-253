def p1():
    return """MainActivity.java
    package com.example.myapplication1;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical">

    <TextView
        android:text="@string/hello_world"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
</LinearLayout>
Strings.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">My Application</string>
    <string name="hello_world">Hello world!</string>
    <string name="action_settings">Settings</string>
</resources>
"""

def p2():
    return """MainActivity.java
    package com.example.myapplication2;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnKeyListener;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText edittext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        addKeyListener();
    }

    public void addKeyListener() {
        edittext = (EditText) findViewById(R.id.editText);
        edittext.setOnKeyListener(new OnKeyListener() {
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if ((event.getAction() == KeyEvent.ACTION_DOWN) &&
                        (keyCode == KeyEvent.KEYCODE_ENTER)) {
                    Toast.makeText(MainActivity.this,
                            edittext.getText(), Toast.LENGTH_LONG).show();
                    return true;
                } else if ((event.getAction() == KeyEvent.ACTION_DOWN) &&
                        (keyCode == KeyEvent.KEYCODE_9)) {
                    Toast.makeText(MainActivity.this,
                            "Number 9 is pressed!", Toast.LENGTH_LONG).show();
                    return true;
                }
                return false;
            }
        });
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical">

    <TextView
        android:text="@string/text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <EditText
        android:id="@+id/editText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
    </EditText>
</LinearLayout>
Strings.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Text Field App</string>
    <string name="text">Enter some text here</string>
    <string name="action_settings">Settings</string>
</resources>
"""

def p3():
    return """MainActivity.java
   package com.example.myapplication3;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private RadioGroup radioGroupGender;
    private RadioButton radioButton;
    private Button btnDisplay;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        addListenerOnButton();
    }

    public void addListenerOnButton() {
        radioGroupGender = (RadioGroup) findViewById(R.id.radioGroupGender);
        btnDisplay = (Button) findViewById(R.id.btnDisplay);

        btnDisplay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int selectedId = radioGroupGender.getCheckedRadioButtonId();
                radioButton = (RadioButton) findViewById(selectedId);
                Toast.makeText(MainActivity.this,
                        radioButton.getText(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical">

    <TextView
        android:text="@string/text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <RadioGroup
        android:id="@+id/radioGroupGender"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content">

        <RadioButton
            android:id="@+id/radioMale"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/radio_male"
            android:checked="true" />

        <RadioButton
            android:id="@+id/radioFemale"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/radio_female" />
    </RadioGroup>

    <Button
        android:id="@+id/btnDisplay"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btn_display" />
</LinearLayout>
Strings.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Radio Button App</string>
    <string name="text">Choose your gender</string>
    <string name="radio_male">Male</string>
    <string name="radio_female">Female</string>
    <string name="btn_display">Display</string>
    <string name="action_settings">Settings</string>
</resources>
"""

def p4():
    return """MainActivity.java
   package com.example.myapplication4;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private CheckBox chkIos, chkAndroid, chkWindows;
    private Button btnDisplay;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        addListenerOnButton();
    }

    public void addListenerOnButton() {
        chkIos = (CheckBox) findViewById(R.id.chkIos);
        chkAndroid = (CheckBox) findViewById(R.id.chkAndroid);
        chkWindows = (CheckBox) findViewById(R.id.chkWindows);
        btnDisplay = (Button) findViewById(R.id.btnDisplay);

        btnDisplay.setOnClickListener(new OnClickListener() {
            // Run when button is clicked
            @Override
            public void onClick(View v) {
                StringBuffer result = new StringBuffer();
                result.append("IPhone check : ").append(chkIos.isChecked());
                result.append("\nAndroid check : ").append(chkAndroid.isChecked());
                result.append("\nWindows Mobile check : ").append(chkWindows.isChecked());

                // Display the result using Toast
                Toast.makeText(MainActivity.this, result.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical">

    <CheckBox
        android:id="@+id/chkIos"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/chk_ios" />

    <CheckBox
        android:id="@+id/chkAndroid"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/chk_android"
        android:checked="true" />

    <CheckBox
        android:id="@+id/chkWindows"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/chk_windows" />

    <Button
        android:id="@+id/btnDisplay"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btn_display" />
</LinearLayout>
Strings.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">CheckBox</string>
    <string name="chk_ios">IPhone</string>
    <string name="chk_android">Android</string>
    <string name="chk_windows">Windows Mobile</string>
    <string name="btn_display">Display</string>
    <string name="action_settings">Settings</string>
</resources>
"""

def p5():
    return """MainActivity.java
  package com.example.myapplication5;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText etNormalText;
    private EditText etPhoneNumber;
    private Button btnSubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        registerViews();
    }

    private void registerViews() {
        etNormalText = findViewById(R.id.et_normal_text);
        etNormalText.addTextChangedListener(new TextWatcher() {
            @Override
            public void afterTextChanged(Editable s) {
                Validation.hasText(etNormalText);
            }

            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }
        });

        etPhoneNumber = findViewById(R.id.et_phone_number);
        etPhoneNumber.addTextChangedListener(new TextWatcher() {
            @Override
            public void afterTextChanged(Editable s) {
                Validation.isPhoneNumber(etPhoneNumber, true);
            }

            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }
        });

        btnSubmit = findViewById(R.id.btn_submit);
        btnSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (checkValidation()) {
                    submitForm();
                } else {
                    Toast.makeText(MainActivity.this, "Form contains error(s)",
                            Toast.LENGTH_LONG).show();
                }
            }
        });
    }

    private void submitForm() {
        Toast.makeText(this, "Submitting form...", Toast.LENGTH_LONG).show();
    }

    private boolean checkValidation() {
        boolean ret = true;
        if (!Validation.hasText(etNormalText)) ret = false;
        if (!Validation.isPhoneNumber(etPhoneNumber, false)) ret = false;
        return ret;
    }
}
validation.java
package com.example.myapplication5;
import android.widget.EditText;
import java.util.regex.Pattern;

public class Validation {
    private static final String PHONE_REGEX = "\\d{3}-\\d{7}";
    private static final String REQUIRED_MSG = "required";
    private static final String PHONE_MSG = "###-#######";

    public static boolean isPhoneNumber(EditText editText, boolean required) {
        return isValid(editText, PHONE_REGEX, PHONE_MSG, required);
    }

    public static boolean isValid(EditText editText, String regex, String errMsg, boolean required) {
        String text = editText.getText().toString().trim();
        editText.setError(null);

        if (required && !hasText(editText)) {
            return false;
        }

        if (!Pattern.matches(regex, text)) {
            editText.setError(errMsg);
            return false;
        }

        return true;
    }

    public static boolean hasText(EditText editText) {
        String text = editText.getText().toString().trim();
        editText.setError(null);

        if (text.length() == 0) {
            editText.setError(REQUIRED_MSG);
            return false;
        }

        return true;
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent">

    <EditText
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:id="@+id/et_normal_text"
        android:hint="Enter Normal Text"
        android:inputType="text"
        android:textStyle="bold"/>

    <EditText
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:id="@+id/et_phone_number"
        android:hint="Enter Phone Number"
        android:inputType="phone"
        android:textStyle="bold"/>

    <Button
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Submit"
        android:id="@+id/btn_submit"/>
</LinearLayout>
"""

def p6():
    return """MainActivity.java
 package com.example.myapplication6;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import android.content.Context;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    EditText inputEt;
    Button btnRead, btnWrite;
    TextView readTv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        inputEt = (EditText) findViewById(R.id.inputEt);
        readTv = (TextView) findViewById(R.id.readTv);
        btnRead = (Button) findViewById(R.id.btnRead);
        btnWrite = (Button) findViewById(R.id.btnWrite);

        btnRead.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View arg0) {
                readTv.setText(getFileContent());
            }
        });

        btnWrite.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View arg0) {
                writeToFile(inputEt.getText().toString());
            }
        });
    }

    private void writeToFile(String text) {
        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(
                    openFileOutput("userinput.txt", Context.MODE_PRIVATE));
            outputStreamWriter.write(text);
            outputStreamWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String getFileContent() {
        String fileContent = "";
        try {
            InputStream inputStream = openFileInput("userinput.txt");
            if (inputStream != null) {
                InputStreamReader inputStreamReader = new InputStreamReader(
                        inputStream);
                BufferedReader bufferedReader = new BufferedReader(
                        inputStreamReader);
                String line = "";
                StringBuilder stringBuilder = new StringBuilder();
                while ((line = bufferedReader.readLine()) != null) {
                    stringBuilder.append(line);
                }
                inputStream.close();
                fileContent = stringBuilder.toString();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        return fileContent;
    }
}
Activity_main.xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="30dp">

        <TextView
            android:id="@+id/textView1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Input text :"
            android:textAppearance="?android:attr/textAppearanceMedium" />

        <EditText
            android:id="@+id/inputEt"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:ems="10"
            android:inputType="textMultiLine">
            <requestFocus />
        </EditText>
    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="30dp">

        <TextView
            android:id="@+id/textView2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Text in file :"
            android:textAppearance="?android:attr/textAppearanceMedium" />

        <TextView
            android:id="@+id/readTv"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="< text from file >"
            android:layout_marginLeft="30dp"/>
    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center"
        android:layout_marginTop="30dp">

        <Button
            android:id="@+id/btnRead"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Read from file" />

        <Button
            android:id="@+id/btnWrite"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Write to file" />
    </LinearLayout>
</LinearLayout>
"""

def p7():
    return """MainActivity.java
 package com.example.myapplication7;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private ImageView imageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.imageView);
        imageView.setOnTouchListener(new TouchListener());

        Toast.makeText(this, "Touch anywhere to change the location of the image",
                Toast.LENGTH_LONG).show();
    }

    private class TouchListener implements View.OnTouchListener {
        float dX, dY;

        @Override
        public boolean onTouch(View view, MotionEvent event) {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    dX = view.getX() - event.getRawX();
                    dY = view.getY() - event.getRawY();
                    break;
                case MotionEvent.ACTION_MOVE:
                    view.animate()
                            .x(event.getRawX() + dX)
                            .y(event.getRawY() + dY)
                            .setDuration(0)
                            .start();
                    break;
                default:
                    return false;
            }
            return true;
        }
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:src="@mipmap/ic_launcher"
        android:scaleType="matrix" />
</LinearLayout>
"""

def p8():
    return """ MainActivity.java
 package com.example.myapplication8;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class CounterActivity extends Activity implements OnClickListener {
    Button startCounter, stopCounter;
    Intent intent = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_counter);

        startCounter = (Button) findViewById(R.id.startCounterButton);
        stopCounter = (Button) findViewById(R.id.stopCounterButton);

        startCounter.setOnClickListener(this);
        stopCounter.setOnClickListener(this);

        intent = new Intent(this, CounterService.class);
    }

    @Override
    public void onClick(View arg0) {
        switch (arg0.getId()) {
            case R.id.startCounterButton:
                startService(intent);
                break;
            case R.id.stopCounterButton:
                stopService(intent);
                break;
            default:
                break;
        }
    }
}
counterservice.java
package com.example.myapplication8;

import android.app.IntentService;
import android.content.Intent;
import android.util.Log;

public class CounterService extends IntentService {
    boolean keepCounting = false;
    int count = 0;

    public CounterService() {
        super("CounterService");
    }

    protected void onHandleIntent(Intent arg0) {
        keepCounting = true;
        count = 0;

        while (keepCounting) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            count++;
            Log.i("CounterStatus", "Time elapsed since service started : " + count + " seconds");
        }
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        Log.i("Service Lifecycle", "onDestroy called");
        count = 0;
        keepCounting = false;
    }
}
Activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center_horizontal"
    android:orientation="vertical"
    tools:context=".CounterActivity"
    tools:ignore="HardcodedText">

    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Counter controls"
        android:layout_marginTop="10dp"
        android:textAppearance="?android:attr/textAppearanceMedium" />

    <LinearLayout
        android:id="@+id/linearLayout1"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp">

        <Button
            android:id="@+id/startCounterButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Start Counter" />

        <Button
            android:id="@+id/stopCounterButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Stop Counter" />
    </LinearLayout>

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="57dp"
        android:text="Counter values are updated in the LogCat"
        android:textAppearance="?android:attr/textAppearanceMedium"/>
</LinearLayout>
AndroidManifest.xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapplication8"
    android:versionCode="1"
    android:versionName="1.0">

    <uses-sdk
        android:minSdkVersion="8"
        android:targetSdkVersion="18" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name">

        <activity
            android:name="com.example.myapplication8.CounterActivity"
            android:exported="true"
            android:label="@string/app_name" >

            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service android:name="CounterService"></service>
    </application>
</manifest>
"""