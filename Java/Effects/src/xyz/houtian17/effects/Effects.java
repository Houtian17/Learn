package xyz.houtian17.effects;

import org.bukkit.command.PluginCommand;
import org.bukkit.plugin.java.JavaPlugin;

public class Effects extends JavaPlugin{
    @Override
    public void onEnable(){
        getCommand("effect").setExecutor(new CommandEffects());
    }
}
