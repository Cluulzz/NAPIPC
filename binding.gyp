{
    "targets": [
        {
            "target_name": "nipc",
            "sources": [
                "src/nipc.cpp"
            ],
            "include_dirs" : [
 	 			 "<!@(node -p \"require('node-addon-api').include\")"
			],
			"dependencies": [
                  "<!(node -p \"require('node-addon-api').gyp\")"
            ]
        }
    ]
}