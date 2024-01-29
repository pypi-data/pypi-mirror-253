#include <dpp/dpp.h>
 
const std::string BOT_TOKEN = "MTE5NzYwNjAwMTQ2NjE1MTAwMg.GvCXMa.RZXvv8iKPuuMkBseASxCCM-Ag_qc18W6wLPak4";
 
int main() {
    dpp::cluster bot(BOT_TOKEN);
 
    bot.on_log(dpp::utility::cout_logger());
 
    bot.on_slashcommand([](const dpp::slashcommand_t& event) {
        if (event.command.get_command_name() == "ping") {
            event.reply("Pong!");
        }

    
	 if (event.command.get_command_name() == "embed") {
	             /* Create an embed */
	             dpp::embed embed = dpp::embed()
		                     .set_color(dpp::colors::sti_blue)
				                     .set_title("Some name")
						                     .set_url("https://dpp.dev/")
								                     .set_author("Some name", "https://dpp.dev/", "https://dpp.dev/DPP-Logo.png")
										                     .set_description("Some description here")
												                     .set_thumbnail("https://dpp.dev/DPP-Logo.png")
														                     .add_field(
																		                         "Regular field title",
																					                     "Some value here"
																							                     )
																                     .add_field(
																				                         "Inline field title",
																							                     "Some value here",
																									                         true
																												                 )
																		                     .add_field(
																						                         "Inline field title",
																									                     "Some value here",
																											                         true
																														                 )
																				                     .set_image("https://dpp.dev/DPP-Logo.png")
																						                     .set_footer(
																										                         dpp::embed_footer()
																													                     .set_text("Some footer text here")
																															                         .set_icon("https://dpp.dev/DPP-Logo.png")
																																		                 )
																								                     .set_timestamp(time(0));
		      
		                 /* Create a message with the content as our new embed. */
		                 dpp::message msg(event.command.channel_id, embed);
				  
				             /* Reply to the user with the message, containing our embed. */
				             event.reply(msg);
					             }
	});
 
    bot.on_ready([&bot](const dpp::ready_t& event) {
        if (dpp::run_once<struct register_bot_commands>()) {
            bot.global_command_create(dpp::slashcommand("ping", "Ping pong!", bot.me.id));
	    bot.global_command_create(dpp::slashcommand("embed", "OMGGGGG!", bot.me.id));
        }
		
    });
 
    bot.start(dpp::st_wait);
}
