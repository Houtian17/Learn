package xyz.houtian17.command;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class CommandHello implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (sender instanceof Player) {
            Player player = (Player) sender;

            if (args.length == 1) {
                switch (args[0]) {
                    case "m8":
                        player.sendMessage("Hi dude");
                        break;
                    case "dude":
                        player.sendMessage("Hi m8");
                        break;
                    default:
                        player.sendMessage("Invalid usage of /hello");
                        break;
                }
            } else {
                player.sendMessage(ChatColor.YELLOW + "Hello");
            }
        }
        return true;
    }
}
