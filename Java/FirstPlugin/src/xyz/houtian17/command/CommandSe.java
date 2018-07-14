package xyz.houtian17.command;

import org.bukkit.Location;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;

public class CommandSe implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (sender instanceof Player) {
            Player p = (Player) sender;
            Location loc=p.getLocation();
            p.getWorld().spawnEntity(loc, EntityType.ZOMBIE);
            p.sendMessage("You spawned in a zombie!");
        }
        return false;

    }
}
