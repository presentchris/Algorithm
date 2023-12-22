package com.example.translation

import android.annotation.SuppressLint
import android.graphics.ImageDecoder
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.MediaStore
import androidx.activity.ComponentActivity
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.activity.result.PickVisualMediaRequest
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.translation.ui.theme.TranslationTheme
import com.google.mlkit.common.model.DownloadConditions
import com.google.mlkit.nl.translate.TranslateLanguage
import com.google.mlkit.nl.translate.Translation
import com.google.mlkit.nl.translate.TranslatorOptions
import androidx.compose.runtime.remember as remember

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            TranslationTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    papago()
                }
            }
        }
    }
}

@SuppressLint("RememberReturnType")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun papago() {

    val enko = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.ENGLISH)
            .setTargetLanguage(TranslateLanguage.KOREAN)
            .build()
        Translation.getClient(options)
    }
    val koen = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.KOREAN)
            .setTargetLanguage(TranslateLanguage.ENGLISH)
            .build()
        Translation.getClient(options)
    }
    val koja = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.KOREAN)
            .setTargetLanguage(TranslateLanguage.JAPANESE)
            .build()
        Translation.getClient(options)
    }
    val jako = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.JAPANESE)
            .setTargetLanguage(TranslateLanguage.KOREAN)
            .build()
        Translation.getClient(options)
    }
    val geko = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.GERMAN)
            .setTargetLanguage(TranslateLanguage.KOREAN)
            .build()
        Translation.getClient(options)
    }
    val koge = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.KOREAN)
            .setTargetLanguage(TranslateLanguage.GERMAN)
            .build()
        Translation.getClient(options)
    }
    val koch = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.KOREAN)
            .setTargetLanguage(TranslateLanguage.CHINESE)
            .build()
        Translation.getClient(options)
    }
    val chko = remember {
        val options = TranslatorOptions.Builder()
            .setSourceLanguage(TranslateLanguage.CHINESE)
            .setTargetLanguage(TranslateLanguage.KOREAN)
            .build()
        Translation.getClient(options)
    }

    var enabled by remember {
        mutableStateOf(false)
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        enko.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        koen.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        jako.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        koja.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        geko.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        koge.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        chko.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }

    LaunchedEffect(Unit) {
        var conditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        koch.downloadModelIfNeeded(conditions)
            .addOnSuccessListener {
                enabled = true
            }
            .addOnFailureListener { exception ->

            }
    }


    var inputText by remember { mutableStateOf("") }
    var translatedText by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        var selectUri by remember {
            mutableStateOf<Uri?>(null)
        }
        val launcher = rememberLauncherForActivityResult(
            contract = ActivityResultContracts.PickVisualMedia(),
            onResult = { uri ->
                selectUri = uri
            })
        if (selectUri != null) {
            val context = LocalContext.current
            val bitmap = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                ImageDecoder.decodeBitmap(
                    ImageDecoder.createSource(context.contentResolver, selectUri!!)
                )
            } else {
                MediaStore.Images.Media.getBitmap(context.contentResolver, selectUri)
            }
            Image(
                bitmap = bitmap.asImageBitmap(),
                contentDescription = ""
            )
        } else {
            Image(
                painter = painterResource(id = R.drawable.mark),
                contentDescription = "phrase"
            )
        }
    }
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
    )


    {
        TextField(
            value = inputText,
            onValueChange = { inputText = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("Enter Something") }
        )
    }

    Spacer(modifier = Modifier.height(15.dp))

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(20.dp)
    ) {
        Text(
            text = if (translatedText.isNotEmpty()) translatedText
            else "Waiting for translation...",
            modifier = Modifier.fillMaxWidth(),
            textAlign = TextAlign.Center,
            fontSize = 30.sp
        )
    }

    Spacer(modifier = Modifier.height(15.dp))

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(30.dp)
    ) {

        Button(
            onClick = {

                enko.translate(inputText)
                    .addOnSuccessListener { result ->
                        translatedText = result
                    }

            },
            enabled = enabled,
            modifier = Modifier.fillMaxWidth(),
        ) {
            Text(text = "English -> Korean")
        }
    }
    Button(
        onClick = {

            koen.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Korean -> English")
    }
    Button(
        onClick = {

            jako.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Japanese -> Korean")
    }
    Button(
        onClick = {

            koja.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Korean -> Japanese")
    }
    Button(
        onClick = {

            geko.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "German -> Korean")
    }
    Button(
        onClick = {

            koge.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Korean -> German")
    }
    Button(
        onClick = {

            chko.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Chinese -> Korean")
    }
    Button(
        onClick = {

            koch.translate(inputText)
                .addOnSuccessListener { result ->
                    translatedText = result
                }

        },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Text(text = "Korean -> Chinese")
    }
    var selectUri by remember {
        mutableStateOf<Uri?>(null)
    }
    val launcher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.PickVisualMedia(),
        onResult = { uri ->
            selectUri = uri
        })
    Button(
        onClick = {
            launcher.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
        },
        modifier = Modifier.size(10.dp),
    ) {
        Text(text = "Image")
    }

}


fun translatedText(input: String): String {
    return "$input"
}

@Preview(showBackground = true)
@Composable
fun Preview() {
    TranslationTheme {
    }
}
