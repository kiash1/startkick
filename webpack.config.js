const path = require("path");


module.exports = {

    entry: {
        'lm_manage_patient/static/lm_manage_patient/js/lm_add_patient': [
            './lifemed_apps/lm_manage_patient/static/lm_manage_patient/js/addPatient.js',


        ],
        'lm_manage_patient/static/lm_manage_patient/js/lm_update_patient': [
            './lifemed_apps/lm_manage_patient/static/lm_manage_patient/js/updatePatient.js',


        ],
        'lm_manage_user/static/lm_manage_user/js/lm_add_user': [
            './lifemed_apps/lm_manage_user/static/lm_manage_user/js/addUser.js',
        ],
         'lm_manage_user/static/lm_manage_user/js/lm_update_user': [
            './lifemed_apps/lm_manage_user/static/lm_manage_user/js/editUser.js',
        ],
         'lm_manage_user/static/lm_manage_user/js/self_update_user': [
            './lifemed_apps/lm_manage_user/static/lm_manage_user/js/editSelfProfile.js',
        ],
        'lm_registration/static/lm_registration/js/lm_registration_minified': [
            './lifemed_apps/lm_registration/static/lm_registration/js/registration.js',
        ],
        'lm_patient_payment/static/lm_patient_payment/js/lm_payment_minified': [
            './lifemed_apps/lm_patient_payment/static/lm_patient_payment/js/payment-list.js',
        ],
         'lm_patient/static/lm_patient/lm_patient_details_minified': [
            './lifemed_apps/lm_patient/static/lm_patient/lm_patient_details.js',
        ],
        'lm_patient/static/lm_patient/lm_patient_security_minified': [
            './lifemed_apps/lm_patient/static/lm_patient/security.js',
        ],

    },
    output: {
        path: path.resolve(__dirname, "./lifemed_apps/"),
        filename: "[name].js"
    },
    module: {
        rules: [
            {
                test: /\.hbs$/,
                use: [{
                    loader: "handlebars-loader",
                    options: {
                        helperDirs: path.resolve(__dirname, "./helpers")
                    }
                }]
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            }
        ]
    },

     // mode: 'development',
    mode: 'production',

    //WATCHER
    watch: true,
    watchOptions: {
        aggregateTimeout: 600,
        ignored: /node_modules/
    },

    //PLUGINS
    plugins: [
    ],
};