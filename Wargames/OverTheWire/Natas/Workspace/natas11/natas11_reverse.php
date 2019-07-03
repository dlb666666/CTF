<?php

    function xorit($plainText, $key) {
        $cipherText = "";
        for($i=0; $i<strlen($plainText); $i++) {
            $cipherText .= $plainText[$i] ^ $key[$i % strlen($key)];
        }
        return $cipherText;
    }

    function analyze_enc_string($data_b64_enc, $plaintext) {
        $data_enc = base64_decode($data_b64_enc);
        $key_hint = xorit($data_enc, $plaintext);
        return $key_hint;
    }

    $enc_strings = array(
                         "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D"=>array("showpassword"=>"no", "bgcolor"=>"#ffffff"),
                         "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFdaAw%3D"=>array("showpassword"=>"no", "bgcolor"=>"#fffffe"),
                        );

    foreach(array_keys($enc_strings) as $enc_string) {
        $json_plaintext = json_encode($enc_strings[$enc_string]);
        print("${enc_string}\n");
        print("{$json_plaintext}\n");
        $key_hint = analyze_enc_string($enc_string, $json_plaintext);
        print("{$key_hint}\n\n");
    }

    $expected_key = "qw8J";
    $crafted_data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
    $encoded_data = base64_encode(xorit(json_encode($crafted_data), $expected_key));
    // DON'T DO THIS: The %3D part was just because of url style base64 encoding.
    // This extra modification would only give us the wrong answer. 
    //$encoded_data = substr($encoded_data, 0, -4);
    //$encoded_data .= "aAw%3D";
    print("\n{$encoded_data}\n");
?>
